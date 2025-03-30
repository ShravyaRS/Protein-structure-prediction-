from Bio import PDB
import requests

# Function to download PDB file
def download_pdb(protein_id):
    url = f"https://files.rcsb.org/download/{protein_id}.pdb"
    response = requests.get(url)
    if response.status_code == 200:
        file_path = f"{protein_id}.pdb"
        with open(file_path, "wb") as file:
            file.write(response.content)
        print(f"✅ Downloaded {protein_id}.pdb successfully!")
        return file_path
    else:
        print("❌ Error: Unable to download PDB file.")
        return None

# Function to parse PDB structure and extract info
def parse_pdb(protein_id, file_path):
    parser = PDB.PDBParser(QUIET=True)
    structure = parser.get_structure(protein_id, file_path)
    print(f"✅ Parsed structure: {protein_id}")

    # Extract useful information
    model = structure[0]  # First model
    chains = list(model.get_chains())  # Get chains
    residues = list(model.get_residues())  # Get residues

    print(f"🔹 Number of Chains: {len(chains)}")
    print(f"🔹 Number of Residues: {len(residues)}")
    return structure

# User input for protein ID
protein_id = input("Enter Protein PDB ID (e.g., 1HHO): ").strip()
file_path = download_pdb(protein_id)

if file_path:
    structure = parse_pdb(protein_id, file_path)
