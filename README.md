This is my catch-all general purpose Discord bot!

## Usage

You'll need to define your secret key in the variable `key` in the module `secrets`. Then, run `bot.py`, and that's
pretty much it.

## Features

### Server Backup

`!update_archive` archives every message in the server, storing them in an SQLite database. Then, you can quickly query the server's messages however you want.

### Bog

- Warns people if Jackson's in the Bog chat all by himself
- Backs up messages in the Bog chat to prepare for deletion
- `!returntobog`

### Reaction Images

Various commands trigger reaction image/copypasta responses.

### Vote to Kick

Can call a vote to kick someone from the voice channel.

### DnD

Various features for when we were playing the DnD space campaign online:

- `!prices`
- `!survival [name]`
- `!travel [light years] [size class] [days || fuel] [use fuel]`
- `!food [population] [dL]`
- Automatic currency conversion: GP <--> (V)