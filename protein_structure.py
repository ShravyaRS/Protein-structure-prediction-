from Bio import PDB
import requests

# Function to download PDB file
def download_pdb(protein_id):
    url = f"https://files.rcsb.org/download/{protein_id}.pdb"
    response = requests.get(url)
    if response.status_code == 200:
        with open(f"{protein_id}.pdb", "wb") as file:  # Use binary mode
            file.write(response.content)
        print(f"✅ Downloaded {protein_id}.pdb successfully!")
    else:
        print("❌ Error: Unable to download PDB file.")

# Function to parse PDB structure
def parse_pdb(protein_id):
    parser = PDB.PDBParser(QUIET=True)
    structure = parser.get_structure(protein_id, f"{protein_id}.pdb")
    print(f"✅ Parsed structure: {protein_id}")
    return structure

# Example protein ID (Hemoglobin - 1HHO)
protein_id = "1HHO"
download_pdb(protein_id)
structure = parse_pdb(protein_id)
