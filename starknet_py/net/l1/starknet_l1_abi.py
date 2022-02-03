STARKNET_L1_ABI = [
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "uint256",
                "name": "from_address",
                "type": "uint256",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "to_address",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256[]",
                "name": "payload",
                "type": "uint256[]",
            },
        ],
        "name": "ConsumedMessageToL1",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "from_address",
                "type": "address",
            },
            {
                "indexed": True,
                "internalType": "uint256",
                "name": "to_address",
                "type": "uint256",
            },
            {
                "indexed": True,
                "internalType": "uint256",
                "name": "selector",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "uint256[]",
                "name": "payload",
                "type": "uint256[]",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "nonce",
                "type": "uint256",
            },
        ],
        "name": "ConsumedMessageToL2",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "uint256",
                "name": "from_address",
                "type": "uint256",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "to_address",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "uint256[]",
                "name": "payload",
                "type": "uint256[]",
            },
        ],
        "name": "LogMessageToL1",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "from_address",
                "type": "address",
            },
            {
                "indexed": True,
                "internalType": "uint256",
                "name": "to_address",
                "type": "uint256",
            },
            {
                "indexed": True,
                "internalType": "uint256",
                "name": "selector",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "uint256[]",
                "name": "payload",
                "type": "uint256[]",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "nonce",
                "type": "uint256",
            },
        ],
        "name": "LogMessageToL2",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "acceptedGovernor",
                "type": "address",
            }
        ],
        "name": "LogNewGovernorAccepted",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "nominatedGovernor",
                "type": "address",
            }
        ],
        "name": "LogNominatedGovernor",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [],
        "name": "LogNominationCancelled",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "operator",
                "type": "address",
            }
        ],
        "name": "LogOperatorAdded",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "operator",
                "type": "address",
            }
        ],
        "name": "LogOperatorRemoved",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "removedGovernor",
                "type": "address",
            }
        ],
        "name": "LogRemovedGovernor",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "bytes32",
                "name": "stateTransitionFact",
                "type": "bytes32",
            }
        ],
        "name": "LogStateTransitionFact",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "globalRoot",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "int256",
                "name": "blockNumber",
                "type": "int256",
            },
        ],
        "name": "LogStateUpdate",
        "type": "event",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "from_address", "type": "uint256"},
            {"internalType": "uint256[]", "name": "payload", "type": "uint256[]"},
        ],
        "name": "consumeMessageFromL2",
        "outputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "finalize",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "identify",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "pure",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "bytes", "name": "data", "type": "bytes"}],
        "name": "initialize",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "isFinalized",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "isFrozen",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "testedOperator", "type": "address"}
        ],
        "name": "isOperator",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "l1ToL2MessageNonce",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "bytes32", "name": "msgHash", "type": "bytes32"}],
        "name": "l1ToL2Messages",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "bytes32", "name": "msgHash", "type": "bytes32"}],
        "name": "l2ToL1Messages",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "programHash",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "newOperator", "type": "address"}
        ],
        "name": "registerOperator",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "to_address", "type": "uint256"},
            {"internalType": "uint256", "name": "selector", "type": "uint256"},
            {"internalType": "uint256[]", "name": "payload", "type": "uint256[]"},
        ],
        "name": "sendMessageToL2",
        "outputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "newProgramHash", "type": "uint256"}
        ],
        "name": "setProgramHash",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "starknetAcceptGovernance",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "starknetCancelNomination",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "testGovernor", "type": "address"}
        ],
        "name": "starknetIsGovernor",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "newGovernor", "type": "address"}
        ],
        "name": "starknetNominateNewGovernor",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "governorForRemoval", "type": "address"}
        ],
        "name": "starknetRemoveGovernor",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "stateBlockNumber",
        "outputs": [{"internalType": "int256", "name": "", "type": "int256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "stateRoot",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "removedOperator", "type": "address"}
        ],
        "name": "unregisterOperator",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256[]", "name": "programOutput", "type": "uint256[]"},
            {"internalType": "uint256", "name": "onchainDataHash", "type": "uint256"},
            {"internalType": "uint256", "name": "onchainDataSize", "type": "uint256"},
        ],
        "name": "updateState",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
]
