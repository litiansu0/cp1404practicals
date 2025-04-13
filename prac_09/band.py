class Band:
    """Band class that 'has' Musicians."""

    def __init__(self, name):
        """Initialize Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def __str__(self):
        """Return string representation of the Band and its musicians."""
        musician_strs = ', '.join(str(m) for m in self.musicians)
        return f"{self.name} ({musician_strs})"

    def play(self):
        """Make each musician play their instrument or indicate if they need one."""
        result = ""
        for musician in self.musicians:
            result += musician.play() + "\n"
        return result.strip()  # Remove the last newline
