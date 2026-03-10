from playwright.sync_api import sync_playwright

def run():
    # clean file
    with open("streams.txt", "w") as streams:
        streams.close()
    
    with open("vdp_links.txt") as f:
        links = [x.strip() for x in f.readlines()]
    
    streams = set()
    
    def capture(page):
    
        def handler(request):
            url = request.url
    
            if ".m3u8" in url:
                if url.endswith("hls.m3u8"):
                    print("FOUND:", url)
                    streams.add(url)
    
        page.on("request", handler)
    
    
    with sync_playwright() as p:
    
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
    
        capture(page)
    
        for link in links:
        
            print("Opening:", link)
    
            page.goto(link)
    
            page.wait_for_timeout(7000)
    
        browser.close()
    
    
    with open("streams.txt", "w") as f:
        for s in streams:
            f.write(s + "\n")
    
    print("Streams saved:", len(streams))