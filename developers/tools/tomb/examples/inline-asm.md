# Inline asm

Inline asm allows to write assembly code that is then inserted and merged into the rest of the code.\
This feature is useful as an workaround for missing features in the compiler.

{% code lineNumbers="true" %}
```csharp
script startup {

	import Call;

	code() {
		local temp:string;
		asm {
			LOAD $temp "hello"
		}
	}
}
```
{% endcode %}
