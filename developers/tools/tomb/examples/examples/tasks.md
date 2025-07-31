# Tasks

A task allows a contract method to run periodically without user intervention.\
Tasks can't have parameters, however you can use Task.current() along with a global Map to associate custom user data to each task.\


{% code lineNumbers="true" %}
```csharp
contract test {
	import Time;
	import Task;

	global victory:bool;
	global deadline:timestamp;

	constructor(owner:address) {
		victory := false;
		time := Time.now() + time.hours(2);
		Task.start(checkResult, owner, 0, TaskFrequency.Always, 999);
	}

	task checkResult()  {
		if (victory) {
			break;
		}

		local now: timestamp := Time.now();

		if (time >= deadline) {
			break;
		}

		continue;
	}

	public win(from:address)
	{
		victory := true;
	}
}

```
{% endcode %}
