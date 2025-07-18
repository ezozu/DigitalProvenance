# DigitalProvenance: Decentralized NFT Marketplace with On-Chain Royalties and Verifiable Metadata

This repository houses the code for DigitalProvenance, a decentralized NFT marketplace designed to provide artists and collectors with a secure and transparent platform for trading digital assets. Built on blockchain technology, DigitalProvenance enforces on-chain royalties, guaranteeing creators are compensated for secondary sales, and leverages IPFS pinning for verifiable metadata, ensuring the longevity and authenticity of NFT information.

DigitalProvenance tackles key issues prevalent in existing NFT marketplaces, such as lack of creator royalty enforcement and potential for metadata manipulation. By implementing royalty logic directly into the smart contracts, we eliminate the reliance on centralized marketplace platforms to honor royalty agreements. Furthermore, the utilization of IPFS and content addressing guarantees that NFT metadata, including artwork and descriptions, remains immutable and accessible even if the original host server goes offline. This enhanced provenance system gives buyers confidence in the authenticity and long-term value of their digital assets.

The platform utilizes a Solidity-based escrow contract system to facilitate secure NFT transfers. When a buyer initiates a purchase, the funds are held in escrow until the NFT is successfully transferred to their wallet. This mechanism provides a level of security for both buyers and sellers, minimizing the risk of fraud or disputes. The marketplace also includes features for listing NFTs, browsing available assets, and managing user profiles, providing a user-friendly experience while maintaining the underlying principles of decentralization and transparency.

DigitalProvenance aims to foster a more equitable and sustainable ecosystem for digital art and collectibles by empowering creators and safeguarding the integrity of the NFT ecosystem. We believe this project represents a significant step towards a truly decentralized and trusted platform for the creation, distribution, and exchange of digital ownership.

## Key Features

*   **On-Chain Royalties Enforcement:** Solidity smart contracts enforce royalty payments to the original creator upon each secondary sale, ensuring artists are continuously compensated for their work. The royalty percentage is embedded within the NFT's metadata and enforced by the smart contract logic. Example: The `_transfer` function in the ERC721 contract includes a check to deduct the royalty percentage from the sale price and transfer it to the designated royalty address.
*   **Verifiable Metadata via IPFS Pinning:** NFT metadata, including artwork and descriptions, is stored on IPFS and pinned to ensure long-term availability. The IPFS hash of the metadata is stored on-chain, providing a verifiable link to the content. An IPFS gateway provides a human-readable interface for accessing the metadata.
*   **Solidity-Based Escrow Contracts:** Secure and transparent transactions are facilitated through Solidity-based escrow contracts, ensuring funds are held until the NFT transfer is confirmed. Upon purchase initiation, funds are locked in the escrow contract; the seller transfers the NFT; and once the buyer confirms receipt, the funds are released to the seller (minus royalties).
*   **Decentralized Listing and Discovery:** Users can list their NFTs for sale directly on the marketplace, leveraging decentralized storage and smart contracts to manage listings. A GraphQL API indexes all on-chain data, allowing for efficient searching and filtering of available NFTs.
*   **User Profile Management:** Users can create and manage their profiles on the platform, including information such as their wallet address, profile picture, and a brief bio. User data is stored in a decentralized manner, typically using IPFS or a similar distributed storage solution, with a hash of the user data stored on-chain.
*   **Open-Source and Community-Driven:** The project is open-source, encouraging community contributions and fostering collaboration to improve the platform. All code is publicly available and licensed under the MIT license.

## Technology Stack

*   **Python:** Used for backend logic, API development, and scripting. Provides the foundation for interacting with blockchain nodes and managing IPFS interactions.
*   **Solidity:** The smart contract language for defining the NFT token standard (ERC721), royalty logic, and escrow contracts. The smart contracts are deployed and executed on the Ethereum blockchain (or a compatible EVM chain).
*   **IPFS (InterPlanetary File System):** A decentralized storage network used for storing NFT metadata, ensuring immutability and long-term availability. Metadata is pinned to prevent garbage collection and ensure permanent storage.
*   **Web3.py:** Python library for interacting with the Ethereum blockchain, enabling communication with smart contracts and retrieving on-chain data.
*   **Ganache/Hardhat:** Used for local blockchain development and testing, allowing developers to simulate the Ethereum environment and test smart contracts.
*   **GraphQL:** An API query language used for efficiently retrieving data from the blockchain and IPFS. It allows clients to request specific data fields, minimizing data transfer and improving performance.

## Installation

1.  **Clone the repository:**
    git clone https://github.com/ezozu/DigitalProvenance.git
    cd DigitalProvenance

2.  **Install Python dependencies:**
    Ensure you have Python 3.7 or higher installed. Then, create a virtual environment:
    python3 -m venv venv
    source venv/bin/activate  (or venv\Scripts\activate on Windows)
    pip install -r requirements.txt

3.  **Install Hardhat (for smart contract deployment and testing):**
    npm install --save-dev hardhat

4.  **Set up IPFS:**
    Ensure IPFS is installed and running locally. You can download it from [https://ipfs.io/](https://ipfs.io/)
    Initialize IPFS: ipfs init
    Start IPFS daemon: ipfs daemon

5.  **Deploy Smart Contracts:**
    Configure Hardhat to connect to your desired network (e.g., Ganache, Sepolia). Modify the hardhat.config.js file accordingly.
    Run the deployment script: npx hardhat run scripts/deploy.js --network <network_name>
    Note the contract addresses generated after deployment.

## Configuration

*   **Environment Variables:**
    Create a `.env` file in the root directory and define the following environment variables:

    *   `WEB3_PROVIDER_URI`: The URI of your Ethereum node (e.g., `http://localhost:8545` for Ganache).
    *   `CONTRACT_ADDRESS`: The address of the deployed NFT smart contract.
    *   `ESCROW_CONTRACT_ADDRESS`: The address of the deployed escrow contract.
    *   `IPFS_GATEWAY`: The URL of your IPFS gateway (e.g., `http://localhost:8080`).
    *   `PRIVATE_KEY`: The private key of the deployer account (used for signing transactions).

*   **hardhat.config.js:**
    Configure the `hardhat.config.js` file to specify the network details for deployment and testing. This includes the network name, URL, and accounts.

## Usage

1.  **Interacting with the Smart Contracts:**

    You can use the `web3.py` library to interact with the deployed smart contracts. Here's an example of how to mint a new NFT:

    from web3 import Web3
    from dotenv import load_dotenv
    import os

    load_dotenv()

    w3 = Web3(Web3.HTTPProvider(os.getenv('WEB3_PROVIDER_URI')))
    contract_address = os.getenv('CONTRACT_ADDRESS')
    private_key = os.getenv('PRIVATE_KEY')
    account_address = w3.eth.account.from_key(private_key).address

    # Assuming you have the ABI of your NFT contract in nft_abi.json
    with open('nft_abi.json', 'r') as f:
        nft_abi = json.load(f)

    contract = w3.eth.contract(address=contract_address, abi=nft_abi)

    # Example: Mint a new NFT
    nonce = w3.eth.get_transaction_count(account_address)
    txn = contract.functions.mintNFT(account_address, "ipfs://YOUR_IPFS_HASH").build_transaction({
        'nonce': nonce,
        'gas': 200000,
        'gasPrice': w3.eth.gas_price
    })
    signed_txn = w3.eth.account.sign_transaction(txn, private_key)
    txn_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    print(f"Transaction hash: {w3.toHex(txn_hash)}")

2.  **IPFS Integration:**

    Use the `ipfshttpclient` library to interact with the IPFS daemon.

    import ipfshttpclient

    client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001')
    res = client.add('path/to/your/nft_metadata.json')
    print(res['Hash']) # This is the IPFS hash you'll store on-chain

3.  **API Documentation (Example):**

    A GraphQL API is used for querying the marketplace data. The API endpoint is `/graphql`.

    Example query to retrieve all listed NFTs:

    query {
      nfts {
        id
        tokenId
        owner
        ipfsHash
        price
      }
    }

## Contributing

We welcome contributions to DigitalProvenance! Please follow these guidelines:

*   Fork the repository.
*   Create a new branch for your feature or bug fix.
*   Write clear and concise commit messages.
*