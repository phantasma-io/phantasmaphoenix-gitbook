# Scripts

## Default

A script is something that can be used either for a transaction or for an API invokeScript call.\
This example showcases a simple script with one argument, that calls a contract.\
Note that for scripts with arguments, for them to run properly you will have to push them into the stack before.

{% code lineNumbers="true" %}
```csharp
script startup {

	import Call;

	code(target:address) {
		local temp:number := 50000;
		Call.contract("Stake", "Unstake", target, temp);
	}
}
```
{% endcode %}



## Deploy contract

This example showcases a script that deploys a token contract.

{% code lineNumbers="true" %}
```csharp
token GHOST {
...
}

script deploy {

    import Token;
    import Module;

    code() {
        local maxSupply:number := 50000;
        local decimals:number := 1;
		local flags:TokenFlags := TokenFlags.None;
        Token.create(@P2KAkQRrL62zYvb5198CHBLiKHKr4bJvAG7aXwV69rtbeSz, "GHOST",  "Ghost Token", maxSupply, decimals, flags, Module.getScript(GHOST),  Module.getABI(GHOST));
    }
}
```
{% endcode %}

## Minting script

This example showcases a script that mints a custom NFT.\


{% code lineNumbers="true" %}
```csharp
struct my_rom_data {
	name:string;
	counter:number;
}

script token_minter {

	import Token;

	code(source:address, target:address) {
		local rom_data:my_rom_data := Struct.my_rom_data("hello", 123);
		NFT.mint(source, target, "LOL", rom_data, "ram_can_be_anything");
	}
}
```
{% endcode %}

###

\


\
