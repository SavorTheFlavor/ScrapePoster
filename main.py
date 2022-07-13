import scraping_modules.reddit as reddit
import scraping_modules.compile as compile
import config


def main():
    source = config.source_list[config.source]
    if source == 'reddit':
        reddit.parse(config.subreddit, config.dl_count)
    compile.compile(config.title)

if __name__ == '__main__':
    main()