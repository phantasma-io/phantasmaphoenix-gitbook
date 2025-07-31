# Call

{% hint style="info" %}
The Call library is an utility library that helps doing all kinds of internal and external method calls. This allows smart contract developers to access unreleased and experimental features and also to do advanced tricks.
{% endhint %}

| Method                                    | Return type | Description                                                                                                                                               |
| ----------------------------------------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Call.interop(...:Generic)                 | Any         | Use this to call any interop method available in Phantasma. For more info read about [Interop Calls](https://docs.phantasma.io/#virtual_machine-interop). |
| Call.contract(method:String, ...:Generic) | Any         | This is used to call another contract with a specified method.                                                                                            |
| Call.method(...:Generic)                  | Any         | To call a method inside the contract, but instead of using `this.methodName()`. eg: Allows to jump to a method based on a string variable.                |

