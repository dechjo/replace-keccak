    PIPENV_VENV_IN_PROJECT=1 pipenv install --dev
    pipenv run python replace-keccak.py ../lido-dao/contracts/0.4.24/oracle/LidoOracle.sol
