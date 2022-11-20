from brownie import accounts, config, SimpleStorage, network


def deploy_simple_storage():
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)

    # account = accounts.add(config["wallets"]["from_key"])
    # print(account)


def main():
    deploy_simple_storage()
    get_account()


def get_account():
    if network.show_active() == "development":
        account = accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
