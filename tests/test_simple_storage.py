from brownie import accounts, SimpleStorage

# arrange
# act
# assert


def test_simple_storage():
    account = accounts[0]
    simplestorage = SimpleStorage.deploy({"from": account})
    starting_value = simplestorage.retrieve()
    print(starting_value)
    updated_value = simplestorage.store(2)
    starting_value = simplestorage.retrieve()
    print(starting_value)

    assert starting_value == 2
