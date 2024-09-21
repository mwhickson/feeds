import unittest
from os import path as ospath

import app

class TestObjectCreation(unittest.TestCase):

    def test_config_create(self):
        c = app.Config()
        self.assertIsNotNone(c.HomeFolder)
        self.assertEqual(ospath.join(c.HomeFolder, "config.ini"), c.ConfigurationFile)
        self.assertEqual("subscriptions.xml", c.SubscriptionFile)
        self.assertEqual("feeds.db", c.DatabaseFile)
        self.assertEqual(60, c.FeedCheckInterval)

    def test_feed_create(self):
        f = app.Feed("A Test Feed", "https://feed.com/test.rss")
        self.assertEqual("A Test Feed", f.Title)
        self.assertEqual("https://feed.com/test.rss", f.Url)
        self.assertEqual(None, f.Status)
        self.assertEqual([], f.Items)

    def test_feeditem_create(self):
        i = app.FeedItem("A Test Article", "https://feed.com/articles/article.html")
        self.assertEqual("A Test Article", i.Title)
        self.assertEqual("https://feed.com/articles/article.html", i.Url)
        self.assertEqual("", i.Content)
        self.assertEqual(None, i.PublishedOn)
        self.assertEqual(None, i.Status)

    def test_feeditemstatus_create(self):
        s = app.FeedItemStatus()
        self.assertEqual(False, s.IsNew)
        self.assertEqual(False, s.IsRead)

    def test_feedstatus_create(self):
        s = app.FeedStatus()
        self.assertEqual(None, s.LastRetrieved)

    def test_subscriptions_create(self):
        s = app.Subscriptions()
        self.assertEqual([], s.Feeds)


if __name__ == "__main__":
    unittest.main()