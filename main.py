from pathlib import Path

from ase.io import read
from ase.visualize import view
from pymatgen.core import Structure

# sets here to the path of the py file
here = Path(__file__).resolve().parent


def main():
    #define paths 
    INPUT_CIF = here / "data" / "catio3_bulk.cif"
    OUTPUT_DIR = here / "outputs"
    OUTPUT_CIF = OUTPUT_DIR / "catio3_supercell.cif"

    #generate supercell from unit cell input
    bulkstructure = Structure.from_file(str(INPUT_CIF))
    supercell = bulkstructure * (2, 2, 2)

    #export the supercell as a CIF in output folder
    OUTPUT_DIR.mkdir(exist_ok=True)
    supercell.to(fmt="cif", filename=str(OUTPUT_CIF))

    #read the exported CIF file
    atoms = read(OUTPUT_CIF)

    #ask user if they want to visualize the supercell & visualize if yes 
    answer = input(f"Would you like to visualize {OUTPUT_CIF.stem}? [y/N] ")
    if answer=="y":
        view(atoms)

if __name__ == "__main__":
    main()