# Task

{% hint style="info" %}
The Task library exposes methods to start and stop [tasks](https://docs.phantasma.info/#chain-tasks).
{% endhint %}

| Method                                                                                | Return type | Description                                                                                                    |
| ------------------------------------------------------------------------------------- | ----------- | -------------------------------------------------------------------------------------------------------------- |
| Task.start(method:Method, from:Address, frequency:Number, mode:Enum, gasLimit:Number) | Task        | Start the task by method name, from the given address and frequency(timestamp), the TaskMode and the gasLimit. |
| Task.stop(task:Address)                                                               | None        | Stop the task method.                                                                                          |
| Task.current()                                                                        | Task        | Returns teh current task method.                                                                               |
