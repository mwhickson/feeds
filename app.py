#
# feeds - a news reader for RSS, Atom or other internet news feeds.
#


class Feed:
    """A news feed in RSS, Atom, or other standardized format."""

    def __init__(self, title: str, url: str) -> None:
        """Construct a Feed with a title and a url."""
        self.Title: str = title
        self.Url: str = url
        self.Status: type[FeedStatus] = None
        self.Items: list[type[FeedItem]] = []


class FeedItem:
    """An article in a news feed."""

    def __init__(self, title: str, url: str) -> None:
        """Construct a FeedItem with a title and a url."""
        self.Title: str = title
        self.Url: str = url
        self.Content: str = ""
        self.PublishedOn = None
        self.Status: type[FeedItemStatus] = None


class FeedItemStatus:
    """The status of a FeedItem (article)."""

    def __init__(self, new: bool = False, read: bool = False) -> None:
        """Construct a FeedItemStatus with its state flags (e.g. new, read)."""
        self.IsNew: bool = new
        self.IsRead: bool = read


class FeedStatus:
    """The status of a Feed."""

    def __init__(self, retrievedOn) -> None:
        """Construct a FeedStatus with its last retrieved date."""
        self.LastRetrieved = retrievedOn


class Subscriptions:
    """A list of Feeds being monitored."""

    def __init__(self, feeds: list[type[Feed]] = []) -> None:
        """Construct Subscriptions with a list of Feeds to monitor."""
        self.Feeds: list[type[Feed]] = feeds


# main


if __name__ == "__main__":
    print("feeds")