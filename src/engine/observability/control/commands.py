class CommandHandler:
    def __init__(self, engine):
        self.engine = engine
        self.commands = {
            "set_food": self._set_food,
            "set_health": self._set_health,
            "set_oxen": self._set_oxen,
            "set_distance": self._set_distance,
            "help": self._help,
            "exit": self._exit
        }

    def execute(self, cmd_line):
        """Parse and execute a command string."""
        parts = cmd_line.strip().split()
        if not parts:
            return "No command entered."
        
        cmd_name = parts[0].lower()
        args = parts[1:]

        if cmd_name in self.commands:
            try:
                return self.commands[cmd_name](*args)
            except TypeError:
                return f"Invalid arguments for '{cmd_name}'."
            except Exception as e:
                return f"Error executing '{cmd_name}': {e}"
        else:
            return f"Unknown command: '{cmd_name}'. Type 'help' for list."

    def _set_food(self, amount):
        self.engine.wagon.food = int(amount)
        return f"Wagon food set to {amount}."

    def _set_health(self, amount):
        self.engine.wagon.health = int(amount)
        return f"Wagon health set to {amount}."

    def _set_oxen(self, amount):
        self.engine.wagon.oxen = int(amount)
        return f"Wagon oxen set to {amount}."

    def _set_distance(self, amount):
        self.engine.wagon.distance_traveled = int(amount)
        return f"Distance set to {amount}."

    def _help(self):
        return f"Available commands: {', '.join(self.commands.keys())}"

    def _exit(self):
        return "EXIT_CONSOLE"
