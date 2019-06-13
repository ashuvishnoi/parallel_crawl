from app.sample_code import sample_core


def test_parallel_crawl():

    s = sample_core.parallel_crawl('https://timesofindia.indiatimes.com/india/bengaluru-firm-to-build-moon-lander-for-nasa-2020-mission/articleshow/69684821.cms',1)
    a = 'https://timesofindia.indiatimes.com/india/bengaluru-firm-to-build-moon-lander-for-nasa-2020-mission/articleshow/69684821.cms'

    assert s[a].title == 'Bengaluru firm to build moon lander for Nasa 2020 mission'

