# Leaderboard

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
