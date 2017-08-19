# Sleepdog

Slack bot for monitoring and notification of filesystem events

## Requirements

- watchdog
- slacker

## Install

```
$ pip install git+https://github.com/yagays/sleepdog
```

## Usage

```sh
$ sleepdog --pattern .json --channel general --token <slack token> --dir log/
```

## Author

@yag_ays
