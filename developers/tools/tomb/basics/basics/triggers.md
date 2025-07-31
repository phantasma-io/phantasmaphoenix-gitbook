# Trigger's

There's a list of available triggers that you can use. They should start with “on” and then the trigger name, for example onMint. They can be `Account` Triggers, `Token` Triggers or `Organization` Triggers.

### **On the `Account` triggers it has:**

1. `OnMint`: This methods will be triggers when you mint.
2. `OnBurn`: This method will be triggered when you burn that token.
3. `OnSend`: This method will be triggered when sending that token.
4. `OnReceive`: This method will be triggered when receiving that token.
5. `OnWitness`: This method will be triggered when you want to prove that was your account to validate that Transaction.
6. `OnUpgrade`: This method will be triggered when upgrading that contract/token.
7. `OnMigrate`: This method will be triggered when migrating.

***

### **On the `Token` triggers it has:**

1. `OnMint`: This method will be triggered when a token is minted.
2. `OnBurn`: This method will be triggered when a token is burned.
3. `OnSend`: This method will be triggered when a token is sent.
4. `OnReceive`: This method will be triggered when a token is received.
5. `OnInfuse`: This method will be triggered when a token is infused.
6. `OnUpgrade`: This method will be triggered when a contract is upgraded.
7. `OnSeries`: This method will be triggered when a series is created.
8. `OnWrite`: This method will be triggered when NFT.Write is called. (When NFT ram is being updated)
9. `OnMigrate`: This method will be triggered when token is migrated.
10. `OnKill`: This method will be triggered when you want to destroy/delete the token.

***

### **On the `Organization` triggers it has:**

1. `OnAdd`: This method will be triggered when adding a contract to the chain.
2. `OnRemove`: This method will be triggered when removing a contract from the chain.
3. `OnUpgrade`: This method will be triggered when upgrading a contract in the chain.

***

### **Relavent information.**

`onMint`, `onBurn`, `onSeed` and `onReceive` share the same parameters,\
&#xNAN;_&#x41;ddress_, _Address_, _string_ and a _number_.

```
trigger onMint(from:address, to:address, symbol:string, tokenID:number) 
trigger onBurn(from:address, to:address, symbol:string, tokenID:number)
trigger onSeed(from:address, to:address, symbol:string, amount:number)
trigger onReceive(from:address, to:address, symbol:string, amount:number)  
```

***

`onWitness`, `onSeries`, `onUpgrade` and `OnKill` share the same parameter,\
&#xNAN;_&#x41;ddress_.

```
trigger onWitness(from:address)
trigger onSeries(from:address)
trigger onUpgrade(from:address) 
trigger onKill(from:address) 
```

***

`onMigrate` parameters are,\
&#xNAN;_&#x41;ddress_ and _Address_.

```
trigger onMigrate(from:address, to:address)
```
