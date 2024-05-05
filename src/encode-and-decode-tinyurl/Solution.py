// https://leetcode.com/problems/encode-and-decode-tinyurl

class Codec:
    allUrls = {}
    def encode(self, longUrl: str) -> str:
        shortUrl = hash(longUrl)
        self.allUrls[shortUrl] = longUrl
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        return self.allUrls[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))