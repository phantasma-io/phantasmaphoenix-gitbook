# Libraries

## Account

{% hint style="info" %}
The Account library exposes methods to handle Phantasma [accounts](https://docs.phantasma.info/#chain-accounts).
{% endhint %}

| Method                                                               | Return type | Description                                                                                                                                                                                                                                                                   |
| -------------------------------------------------------------------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Account.getName(from:Address)                                        | String      | Returns the name of an account associated to the specified address, if any.                                                                                                                                                                                                   |
| Account.getLastActivity(from:Address)                                | Timestamp   | Returns a timestamp of the last known activity of the specified address.                                                                                                                                                                                                      |
| Account.registerName(target:Address, name:String)                    | None        | Registers a name for the specified address. Names must be fit specified rules (TODO write rules here). Must have a stake of at least 2 SOUL.                                                                                                                                  |
| Account.unregisterName(target:Address)                               | None        | Unregisters a name from an account. After unregistering, the name becomes available to use in other addresses.                                                                                                                                                                |
| Account.registerScript(target:Address, script:Bytes, abiBytes:Bytes) | None        | Registers an account script to the specified address. An account script can contain multiple triggers for custom account behaviours.                                                                                                                                          |
| Account.hasScript(address:Address)                                   | Bool        | Returns true if the specified address has an account script registered to it.                                                                                                                                                                                                 |
| Account.lookUpScript(target:Address)                                 | Bytes       | Returns the script of an account, if a script is registered.                                                                                                                                                                                                                  |
| Account.lookUpABI(target:Address)                                    | Bytes       | Returns the ABI of an account script, if a script is registered.                                                                                                                                                                                                              |
| Account.lookUpName(name:String)                                      | Address     | Returns the address that registered the specified name, if any.                                                                                                                                                                                                               |
| Account.migrate(from:Address, target:Address)                        | None        | Migrates an account from one address to another. This will migrate everything, including stakes, storage and DAO memberships. Also any other contracts that support account migration will also receive a migration trigger (allowing them migrate data or do other actions). |

## Address

| Method                            | Return type | Description                                                            |
| --------------------------------- | ----------- | ---------------------------------------------------------------------- |
| Address.isNull(target:Address)    | Bool        | Returns true if the address is null, false otherwise.                  |
| Address.isUser(target:Address)    | Bool        | Returns true if the address is a user, false otherwise.                |
| Address.isSystem(target:Address)  | Bool        | Returns true if the address is a System address, false otherwise.      |
| Address.isInterop(target:Address) | Bool        | Returns true if the address is an Internal Operation, false otherwise. |

## Array

{% hint style="info" %}
The Array library exposes methods to manipulate arrays. It is also possible to manipulate arrays directly via TOMB array variables.
{% endhint %}

| Method                                               | Return type | Description                                                          |
| ---------------------------------------------------- | ----------- | -------------------------------------------------------------------- |
| Array.get(array:Any, index:Number)                   | Generic<0>  | Returns the element of an array at the given index.                  |
| Array.set(array:Any, index:Number, value:Generic<0>) | None        | Set the element of an array at the given index with the given value. |
| Array.remove(array:Any, index:Number)                | None        | Removes the element of an array at the given index.                  |
| Array.clear(array:Any)                               | None        | Clears all the Array entries.                                        |
| Array.length(array:Any)                              | Number      | Returns the number of elements in the Array.                         |

## Call

{% hint style="info" %}
The Call library is an utility library that helps doing all kinds of internal and external method calls. This allows smart contract developers to access unreleased and experimental features and also to do advanced tricks.
{% endhint %}

| Method                                    | Return type | Description                                                                                                                                               |
| ----------------------------------------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Call.interop(...:Generic)                 | Any         | Use this to call any interop method available in Phantasma. For more info read about [Interop Calls](https://docs.phantasma.info/#virtual_machine-interop). |
| Call.contract(method:String, ...:Generic) | Any         | This is used to call another contract with a specified method.                                                                                            |
| Call.method(...:Generic)                  | Any         | To call a method inside the contract, but instead of using `this.methodName()`. eg: Allows to jump to a method based on a string variable.                |

## Crowdsale

{% hint style="info" %}
The Crowdsale library exposes methods to create and manage a decentralized crowdsale.
{% endhint %}

| Method                                                                                                                                                                                                                                          | Return type | Description                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ----------------------------------------------------------------------------------------- |
| Crowdsale.create(from:Address, name:String, SaleFlags flags, startDate:Timestamp, endDate:Timestamp, sellSymbol:String, receiveSymbol:String, price:Number, globalSoftCap:Number, globalHardCap:Number, userSoftCap:Number, userHardCap:Number) | Hash        | Returns a Hash of the sale created.                                                       |
| Crowdsale.isSaleActive(saleHash:Hash)                                                                                                                                                                                                           | bool        | Returns true if the sale is active, false otherwise.                                      |
| Crowdsale.GetSaleParticipants(saleHash:Hash)                                                                                                                                                                                                    | Address\[]  | Returns an Array of the addressess in by the saleHash.                                    |
| Crowdsale.getSaleWhitelists(saleHash:Hash)                                                                                                                                                                                                      | Address\[]  | Retruns the list of addresses whitelisted for the sale, by the saleHash.                  |
| Crowdsale.isWhitelisted(saleHash:Hash, address:Address)                                                                                                                                                                                         | Bool        | Returns true if the user is whitelisted for the sale, false otherwise.                    |
| Crowdsale.addToWhitelist(saleHash:Hash, target:Address)                                                                                                                                                                                         | None        | To add a Address to the participate in the sale, by the saleHash and target address.      |
| Crowdsale.removeFromWhitelist(saleHash:Hash, target:Address)                                                                                                                                                                                    | None        | To remove a Address from the participate in the sale, by the saleHash and target address. |
| Crowdsale.getPurchasedAmount(saleHash:Hash, address:Address)                                                                                                                                                                                    | Number      | Returns the Purchased amount.                                                             |
| Crowdsale.getSoldAmount(saleHash:Hash)                                                                                                                                                                                                          | Number      | Returns the amount that the sale has been sold.                                           |
| Crowdsale.purchase(from:Address, saleHash:Hash, quoteSymbol:string, quoteAmount:Number)                                                                                                                                                         | None        | To purchase the sale.                                                                     |
| Crowdsale.closeSale(from:Address, saleHash:Hash)                                                                                                                                                                                                | None        | To close a given saleHash.                                                                |
| Crowdsale.getLatestSaleHash()                                                                                                                                                                                                                   | Hash        | Returns the last saleHash.                                                                |
| Crowdsale.EditSalePrice(saleHash:Hash, price:Number)                                                                                                                                                                                            | None        | To edit the sale price by the saleHash.                                                   |

## Decimal

| Method                                              | Return type | Description                                              |
| --------------------------------------------------- | ----------- | -------------------------------------------------------- |
| Decimal.decimals(target:Any)                        | Number      | Returns the number of decimals of the given target.      |
| Decimal.convert(decimalPlaces:Number, value:Number) | Number      | Returns the converted value of the given decimal places. |

## Enum

| Method                                 | Return type | Description                                       |
| -------------------------------------- | ----------- | ------------------------------------------------- |
| Enum.isSet(target:Enum<>, flag:Enum<>) | Bool        | Returns true if the enum is set, false otherwise. |

## Format

| Method                                       | Return type | Description                                                   |
| -------------------------------------------- | ----------- | ------------------------------------------------------------- |
| Format.decimals(value:Number, symbol:String) | String      | Returns a string with the value formated to the given symbol. |
| Format.symbol(symbol:String)                 | String      | Returns a string representation of the given symbol.          |
| Format.account(address:Address)              | String      | Returns a String with the account formated to print.          |

## Governance

{% hint style="info" %}
The Governance library allows to interact with the decentralized [governance](https://docs.phantasma.info/#chain-governance) of Phantasma.
{% endhint %}

| Method                                                                           | Return type | Description                                                                                                                        |
| -------------------------------------------------------------------------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Governance.hasName(name:String)                                                  | bool        | Returns true if a specific governance tag exists, false otherwise.                                                                 |
| Governance.createValue(name:String, initial:Number, serializedConstraints:Bytes) | None        | Creates a new governance tag and assigns an inital value to it, alongside optional contraints.                                     |
| Governance.getValue(name:String)                                                 | Number      | Returns the current value of a governance tag.                                                                                     |
| Governance.setValue(name:String, value:Number)                                   | None        | Alters the value of a governance tag. Consensus on the change must be achieved before calling this method, otherwise it will fail. |

## Leaderboard

{% hint style="info" %}
The leaderboard library exposes methods that allow to create and manipulate [leaderboards](https://docs.phantasma.info/#chain-leaderboards).
{% endhint %}

| Method                                                                           | Return type | Description                                                                              |
| -------------------------------------------------------------------------------- | ----------- | ---------------------------------------------------------------------------------------- |
| Leaderboard.create(from:Address, boardName:String, capacity:Number)              | None        | To create a new leaderboard by the given address with a board name and a given capacity. |
| Leaderboard.getAddress(boardName:String, index:Number)                           | Address     | Returns the address of the leaderboard, by the given board name and index.               |
| Leaderboard.getScoreByIndex(boardName:String, index:Number)                      | Number      | Returns the score that position, by the given board name and index.                      |
| Leaderboard.getScoreByAddress(boardName:String, target:Address)                  | Number      | Returns the score of the address, by the given board name and the target address.        |
| Leaderboard.getSize(boardName:String)                                            | Number      | Returns the size of the Leaderboard, by the given board name.                            |
| Leaderboard.insert(from:Address, target:Address, boardName:String, score:Number) | None        | To insert a score into the Leaderboard, by the target address, board name and score.     |
| Leaderboard.reset(from:Address, boardName:String)                                | None        | To reset the Leaderboard, by the address and board name.                                 |

## List

| Method                                    | Return type | Description                               |
| ----------------------------------------- | ----------- | ----------------------------------------- |
| List.get(index:Number)                    | Generic     | Returns the element at the given index.   |
| List.add(value:Generic)                   | None        | To add the value to the list.             |
| List.replace(index:Number, value:Generic) | None        | Replaces the value at the given index.    |
| List.remove(index:Number)                 | None        | Removes from the list at a given index.   |
| List.count()                              | Number      | Returns the number of entries in the List |
| List.clear()                              | None        | Clears all the entries in the List        |

## Mail

| Method                                                           | Return type | Description                                                   |
| ---------------------------------------------------------------- | ----------- | ------------------------------------------------------------- |
| Mail.pushMessage(from:Address, target:Address, archiveHash:Hash) | None        | To push a message to the target user mailbox.                 |
| Mail.domainExists(domainName:String)                             | Bool        | Returns true if the specified domain exists, false otherwise. |
| Mail.registerDomain(from:Address, domainName:String)             | None        | To register a domain, from an address and a domain name.      |
| Mail.unregisterDomain(domainName:String)                         | None        | To unregister a domain name.                                  |
| Mail.migrateDomain(domainName:String, target:Address)            | None        | To migrate a domain to a new Address.                         |
| Mail.joinDomain(from:Address, domainName:String)                 | None        | To a user join a domain.                                      |
| Mail.leaveDomain(from:Address, domainName:String)                | None        | To a user leave a domain.                                     |
| Mail.getUserDomain(target:Address)                               | String      | To the the user domain.                                       |

## Map

| Method                              | Return type | Description                               |
| ----------------------------------- | ----------- | ----------------------------------------- |
| Map.get(key:Generic)                | Generic     | Returns the value by the given key.       |
| Map.set(key:Generic, value:Generic) | None        | Set's the value to the specified key.     |
| Map.remove(key:Generic)             | None        | Removes the key from the map.             |
| Map.clear()                         | None        | Clears all the Map entries.               |
| Map.count()                         | Number      | Returns the number of entries in the Map. |
| Map.has(key:Generic)                | Bool        | Returns if the key exists in the Map.     |

## Market

{% hint style="info" %}
The Market library exposes access to methods that allow to buy and sell NFts (including auctions) in shared liquidity NFT markets of Phantasma.
{% endhint %}

| Method                                                                                                                                                                                                                                                 | Return type | Description                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- | ----------------------------------------------------- |
| Market.sell(from:Address, baseSymbol:String, quoteSymbol:String, tokenID:Number, price:Number, endDate:Timestamp)                                                                                                                                      | None        | To sell an NFT, by the tokenID.                       |
| Market.buy(from:Address, symbol:String, tokenID:Number)                                                                                                                                                                                                | None        | To buy an NFT, by the tokenID.                        |
| Market.cancel(symbol:String, tokenID:Number)                                                                                                                                                                                                           | None        | To cancel a Sell.                                     |
| Market.hasAuction(symbol:String, tokenID:Number)                                                                                                                                                                                                       | Bool        | Returns true if has an auction for the given tokenID. |
| Market.bid(from:Address, symbol:String, tokenID:Number, price:Number, buyingFee:Number, buyingFeeAddress:Address)                                                                                                                                      | None        | To bid for the given tokenID.                         |
| Market.listToken(from:Address, baseSymbol:String, quoteSymbol:String, tokenID:Number, price:Number, endPrice:Number, startDate:Timestamp, endDate:Timestamp, extensionPeriod:Number, typeAuction:Number, listingFee:Number, listingFeeAddress:Address) | None        | To list the token by the TokenID.                     |
| Market.editAuction(from:Address, baseSymbol:String, quoteSymbol:String, tokenID:Number, price:Number, endPrice:Number, startDate:Timestamp, endDate:Timestamp, extensionPeriod:Number)                                                                 | None        | To edit the auction for the given tokenID.            |

## Math

{% hint style="info" %}
The Math library exposes methods that do mathematical operations.
{% endhint %}

| Method                       | Return type | Description                                              |
| ---------------------------- | ----------- | -------------------------------------------------------- |
| Math.min(a:Number, b:Number) | Number      | Returns smallest of two numbers                          |
| Math.max(a:Number, b:Number) | Number      | Returns largest of two numbers                           |
| Math.sqrt(x:Number)          | Number      | Returns an integer aproximation of the square root of X. |

## Module

| Method                          | Return type | Description                                       |
| ------------------------------- | ----------- | ------------------------------------------------- |
| Module.getScript(target:Module) | Bytes       | Returns raw bytes containing a serialized module. |
| Module.getABI(target:Module)    | Bytes       | Returns raw bytes containing a serialized ABI.    |

## NFT

{% hint style="info" %}
The NFT library exposes methods that allow minting, burning, [infusing](https://docs.phantasma.info/#nft-infusion) and transfering Phantasma NFTs.
{% endhint %}

| Method                                                                                                  | Return type | Description                                                                               |
| ------------------------------------------------------------------------------------------------------- | ----------- | ----------------------------------------------------------------------------------------- |
| NFT.transfer(from:Address, to:Address, symbol:String, id:Number)                                        | None        | Transfer an NFT from one address to another, by the nftID and symbol.                     |
| NFT.mint(from:Address, to:Address, symbol:String, rom:Any, ram:Any, seriesID:Number)                    | None        | Mint an NFT from one address to another, with the specific ROM and RAM, and the seriesID. |
| NFT.write(from:Address, symbol:String, tokenID:Number, ram:Any)                                         | None        | Write NFT is to update the RAM inside the NFT by the nftID.                               |
| NFT.burn(from:Address, symbol:String, id:Number)                                                        | None        | Burn the nft by the NFTID.                                                                |
| NFT.infuse(from:Address, symbol:String, id:Number, infuseSymbol:String, infuseValue:Number)             | None        | Infuse the NFT with other tokens/NFT with a given amount.                                 |
| NFT.createSeries(from:Address, symbol:String, seriesID:Number, maxSupply:Number, mode:Enum, nft:Module) | None        | Creates a series of NFTs.                                                                 |
| NFT.readROM(symbol:String, id:Number)                                                                   | T           | Returns the ROM by the NFTID.                                                             |
| NFT.readRAM(symbol:String, id:Number)                                                                   | T           | Returns the RAM by the NFTID.                                                             |

## Oracle

{% hint style="info" %}
The Oracle library exposes access to the [oracle](https://docs.phantasma.info/#chain-oracles) features of Phantasma
{% endhint %}

| Method                                                             | Return type | Description                                                                                       |
| ------------------------------------------------------------------ | ----------- | ------------------------------------------------------------------------------------------------- |
| Oracle.read(url:String)                                            | None        | Executes an URL read via oracles. The URL must be a valid Phantasma Oracle URL.                   |
| Oracle.price(symbol:String)                                        | None        | Reads the current price of the given symbol via oracles.                                          |
| Oracle.quote(baseSymbol:String, quoteSymbol:String, amount:Number) | None        | Returns the current price converted to the given quote symbol with the given amount, via oracles. |

## Organization

{% hint style="info" %}
The Organization library allows access to methods to handle [DAOs](https://docs.phantasma.info/#chain-organizations)
{% endhint %}

| Method                                                                  | Return type | Description                                                                                    |
| ----------------------------------------------------------------------- | ----------- | ---------------------------------------------------------------------------------------------- |
| Organization.create(from:Address, id:String, name:String, script:Bytes) | None        | Creates a new DAO. The creator address will be automatically added as part of the DAO members. |
| Organization.addMember(from:Address, name:String, target:Address)       | None        | Adds a new member to a DAO.                                                                    |

## Relay

{% hint style="info" %}
The Relay library exposes methods to access the off-chain message relay system.
{% endhint %}

| Method                                           | Return type | Description |
| ------------------------------------------------ | ----------- | ----------- |
| Relay.getBalance(from:Address)                   | Number      | TODO        |
| Relay.getIndex(from:Address, to:Address)         | Number      | TODO        |
| Relay.getTopUpAddress(from:Address)              | Address     | TODO        |
| Relay.openChannel(from:Address, publicKey:Bytes) | None        | TODO        |
| Relay.getKey(from:Address)                       | Bytes       | TODO        |
| Relay.topUpChannel(from:Address, count:Number)   | None        | TODO        |
| Relay.settleChannel(receipt:RelayReceipt)        | None        | TODO        |

## Runtime

<table><thead><tr><th width="367.3333333333333">Method</th><th width="127">Return type</th><th width="253.66666666666669">Description</th></tr></thead><tbody><tr><td>Runtime.expect(condition:Bool, error:String)</td><td>None</td><td>Does nothing if the condition is true, otherwise terminates execution with the specified error message.</td></tr><tr><td>Runtime.log(message:String)</td><td>None</td><td>To log a message.</td></tr><tr><td>Runtime.isWitness(address:Address)</td><td>Bool</td><td>Check if the specified address was witness to the transaction (eg: the address signed the transaction). Multiple addresses can be witness in the case of the multi-signature transactions.</td></tr><tr><td>Runtime.isTrigger()</td><td>Bool</td><td>Returns true if current code is being ran inside trigger, returns false otherwise.</td></tr><tr><td>Runtime.transactionHash()</td><td>Hash</td><td>Returns the hash of the current executing transaction, if any.</td></tr><tr><td>Runtime.deployContract(from:Address, contract:Module)</td><td>None</td><td>Deploys a contract into the current chain.</td></tr><tr><td>Runtime.upgradeContract(from:Address, contract:Module)</td><td>None</td><td>Upgrades an existing contract, if the contract allows it.</td></tr><tr><td>Runtime.gasTarget()</td><td>Address</td><td>Returns the address that will receive part of the gas fees for the current transaction. A "Gas escrow" event must have happened already otherwise it will return an null address.</td></tr><tr><td>Runtime.context()</td><td>String</td><td>Returns the name of the current executing context. eg: Use this to validate that the current code can only be executed from a specific place.</td></tr><tr><td>Runtime.previousContext()</td><td>String</td><td>Returns the name of the caller context, if any. eg: Use this to validate that the current code can only be executed from a specific place.</td></tr></tbody></table>

## Stake

| Method                                                                               | Return type | Description                                                                      |
| ------------------------------------------------------------------------------------ | ----------- | -------------------------------------------------------------------------------- |
| Stake.getMasterThreshold()                                                           | Number      | Equivalent to calling Governance.getValue() for "MasterStakeThresholdTag".       |
| Stake.isMaster(address:Address)                                                      | bool        | Returns true if the specified address is a SOUL master, returns false otherwise. |
| Stake.getMasterCount()                                                               | Number      | Return current number of SOUL masters.                                           |
| Stake.getClaimMasterCount(claimDate:Timestamp)                                       | Number      | Returns how much SOUL is claimable via a master claim.                           |
| Stake.getMasterClaimDate(claimDistance:Number)                                       | Timestamp   | TODO                                                                             |
| Stake.getMasterDate(target:Address)                                                  | Timestamp   | TODO                                                                             |
| Stake.getMasterClaimDateFromReference(claimDistance:Number, referenceTime:Timestamp) | Timestamp   | TODO                                                                             |
| Stake.getMasterRewards(address:Address)                                              | Number      | TODO                                                                             |
| Stake.masterClaim(from:Address)                                                      | None        | TODO                                                                             |
| Stake.stake(from:Address, stakeAmount:Number)                                        | None        | To stake an amount to the the address with the stake amount.                     |
| Stake.unstake(from:Address, unstakeAmount:Number)                                    | None        | To unstake an amount to the the address with the unstake amount.                 |
| Stake.getTimeBeforeUnstake(from:Address)                                             | Number      | TODO                                                                             |
| Stake.getStakeTimestamp(from:Address)                                                | Timestamp   | Returns timestamp of last stake for the specified address.                       |
| Stake.getUnclaimed(from:Address)                                                     | Number      | Returns the unclaimed KCAL amount for the specified address.                     |
| Stake.claim(from:Address, stakeAddress:Address)                                      | None        | Claims the the staked rewards for the given stake address.                       |
| Stake.getStake(address:Address)                                                      | Number      | Returns how much SOUL is staked at the specified address.                        |
| Stake.getStorageStake(address:Address)                                               | Number      | Returns how much SOUL is locked due to being used for storage.                   |
| Stake.fuelToStake(fuelAmount:Number)                                                 | Number      | Converts KCAL amount to SOUL.                                                    |
| Stake.stakeToFuel(stakeAmount:Number)                                                | Number      | Converts SOUL amount to KCAL.                                                    |
| Stake.getAddressVotingPower(address:Address)                                         | Number      | Returns the normalized voting power of an address.                               |

## Storage

{% hint style="info" %}
The Storage library allows a contract to interact with contract storage and also the decentralized [file storage](https://docs.phantasma.info/#chain-storage) of Phantasma.
{% endhint %}

| Method                                                                                                             | Return type | Description                                                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------ | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Storage.read(contract:String, field:String)                                                                        | Generic     | Reads a field from a contract.                                                                                                                                                                                                 |
| Storage.write(field:String, value:Any)                                                                             | None        | Writes a field value. Due to security reasons, it's not possible to specify a contract, instead the current contract is used. If the current context is not a valid contract or is a read-only context, this method will fail. |
| Storage.delete(field:String)                                                                                       | None        | Deletes a field. Same rules as Storage.write()                                                                                                                                                                                 |
| Storage.calculateStorageSizeForStake(stakeAmount:Number)                                                           | Number      | Converts amount of staked SOUL into kilobytes of storage.                                                                                                                                                                      |
| Storage.createFile(target:Address, fileName:String, fileSize:Number, contentMerkle:Bytes, encryptionContent:Bytes) | None        | Creates a new decentralized file in the target address account. Note that since in Phantasma the actual file contents are not stored in the chain, only a content merkle should be provided.                                   |
| Storage.hasFile(target:Address, hash:Hash)                                                                         | Bool        | Returns true if the target is storing a file with the specified hash, false otherwise.                                                                                                                                         |
| Storage.addFile(from:Address, target:Address, archiveHash:Hash)                                                    | None        | Copies a file with the specified hash into the target address storage.                                                                                                                                                         |
| Storage.deleteFile(from:Address, targetHash:Hash)                                                                  | None        | Deletes the file with the specified hash from the specified address storage.                                                                                                                                                   |
| Storage.hasPermission(externalAddr:Address, target:Address)                                                        | Bool        | Returns true if external address has permission to add files to target address, false otherwise.                                                                                                                               |
| Storage.addPermission(from:Address, externalAddr:Address)                                                          | None        | Adds permission to external address to add files to from address storage.                                                                                                                                                      |
| Storage.deletePermission(from:Address, externalAddr:Address)                                                       | None        | Removes permission from external address to add files to from address storage.                                                                                                                                                 |
| Storage.getUsedSpace(from:Address)                                                                                 | Number      | Returns how many kilobytes are being used as storage by the specified address.                                                                                                                                                 |
| Storage.getAvailableSpace(from:Address)                                                                            | Number      | Returns how many kilobytes are being available as storage by the specified address.                                                                                                                                            |

## String

| Method                                                    | Return type | Description                                                                                 |
| --------------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------- |
| String.toBytes(target:String)                             | Bytes       | To convert a given string into a byte array, and returns it.                                |
| String.length(target:String)                              | Number      | Returns the length of the string.                                                           |
| String.substr(target:String, index:Number, length:Number) | String      | Returns the substring of the given string at an index and a length.                         |
| String.toArray(target:String)                             | Array       | To convert the String into an Array of Numbers that represent each Character in the String. |
| String.fromArray(target:Array)                            | String      | To convert a given Array into a String, each number represents a Character.                 |
| String.toUpper(target:String)                             | String      | Returns a new string with all characters in uppercase.                                      |
| String.toLower(target:String)                             | String      | Returns a new string with all characters in lowercase.                                      |
| String.indexOf(target:String, ch:Number)                  | Number      | Returns the index of the first occurence of the character or -1 if not found.               |

## Task

{% hint style="info" %}
The Task library exposes methods to start and stop [tasks](https://docs.phantasma.info/#chain-tasks).
{% endhint %}

| Method                                                                                | Return type | Description                                                                                                    |
| ------------------------------------------------------------------------------------- | ----------- | -------------------------------------------------------------------------------------------------------------- |
| Task.start(method:Method, from:Address, frequency:Number, mode:Enum, gasLimit:Number) | Task        | Start the task by method name, from the given address and frequency(timestamp), the TaskMode and the gasLimit. |
| Task.stop(task:Address)                                                               | None        | Stop the task method.                                                                                          |
| Task.current()                                                                        | Task        | Returns teh current task method.                                                                               |

## Time

{% hint style="info" %}
The Time library provides methods to initialize timestamp variables.
{% endhint %}

| Method                  | Return type | Description                                           |
| ----------------------- | ----------- | ----------------------------------------------------- |
| Time.now()              | Timestamp   | Returns the current time.                             |
| Time.unix(value:Number) | Timestamp   | Returns a timestamp from an Unix time (32 bit value). |

## Token

{% hint style="info" %}
The Token library allows contracts to create and transfer fungible tokens.\
While some of the methods here also work for non-fungible tokens, see also the [NFT](https://docs.phantasma.info/#nft-library) library.
{% endhint %}

| Method                                                                                                                           | Return type | Description                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Token.create(from:Address, symbol:String, name:String, maxSupply:Number, decimals:Number, flags:Number, script:Bytes, abi:Bytes) | None        | Method used to create a new token. Note, as an exception, NFT are also created with this method.                                                                                     |
| Token.exists(symbol:String)                                                                                                      | Bool        | Returns true if the token exists and false otherwise. Also works for NFTs.                                                                                                           |
| Token.getDecimals(symbol:String)                                                                                                 | Number      | Returns the number of decimals of the token. For NFTs returns zero.                                                                                                                  |
| Token.getFlags(symbol:String)                                                                                                    | Enum        | Returns an Enum with the TokenFlag of the token.                                                                                                                                     |
| Token.transfer(from:Address, to:Address, symbol:String, amount:Number)                                                           | None        | Transfers tokens from one Address, to another address with a specific symbol and the desired amount.                                                                                 |
| Token.transferAll(from:Address, to:Address, symbol:String)                                                                       | None        | Transfer all tokens from one Address, to another address with a specific symbol.                                                                                                     |
| Token.mint(from:Address, to:Address, symbol:String, amount:Number)                                                               | None        | Mints tokens from one Address, to another address with a specific symbol and the desired amount.                                                                                     |
| Token.write(from:Address, symbol:String, tokenID:Number, ram:Any)                                                                | None        | Updates the Token/NFT RAM with the given RAM.                                                                                                                                        |
| Token.burn(from:Address, symbol:String, amount:Number)                                                                           | None        | Burn tokens from the given address, given symbol and the desired amount.                                                                                                             |
| Token.swap(targetChain:String, source:Address, destination:Address, symbol:String, amount:Number)                                | Number      | Converts the specified amount of a token into other token. The returned value is the new amount, which is calculated based on current monetary values of both tokens (if available). |
| Token.getBalance(from:Address, symbol:String)                                                                                    | Number      | Returns the token balance of the specified address.                                                                                                                                  |
| Token.isMinter(address:Address, symbol:String)                                                                                   | Bool        | Returns true if the address has Minter permissions for the specified toen symbol, returns false otherwise.                                                                           |

## UID

| Method         | Return type | Description                  |
| -------------- | ----------- | ---------------------------- |
| UID.generate() | Number      | Returns a unique identifier. |

## Utils

{% hint style="info" %}
The Utils library exposes access to some utility methods that don't fit in other libraries.
{% endhint %}

| Method                             | Return type | Description |
| ---------------------------------- | ----------- | ----------- |
| Utils.contractAddress(name:String) | Address     | TODO        |
