# Raw Files Plugin for [DocPad](http://docpad.org)

<!-- BADGES/ -->

[![Build Status](https://img.shields.io/travis/docpad/docpad-plugin-raw/master.svg)](http://travis-ci.org/docpad/docpad-plugin-raw "Check this project's build status on TravisCI")
[![NPM version](https://img.shields.io/npm/v/docpad-plugin-raw.svg)](https://npmjs.org/package/docpad-plugin-raw "View this project on NPM")
[![NPM downloads](https://img.shields.io/npm/dm/docpad-plugin-raw.svg)](https://npmjs.org/package/docpad-plugin-raw "View this project on NPM")
[![Dependency Status](https://img.shields.io/david/docpad/docpad-plugin-raw.svg)](https://david-dm.org/docpad/docpad-plugin-raw)
[![Dev Dependency Status](https://img.shields.io/david/dev/docpad/docpad-plugin-raw.svg)](https://david-dm.org/docpad/docpad-plugin-raw#info=devDependencies)<br/>
[![Gratipay donate button](https://img.shields.io/gratipay/docpad.svg)](https://www.gratipay.com/docpad/ "Donate weekly to this project using Gratipay")
[![Flattr donate button](https://img.shields.io/badge/flattr-donate-yellow.svg)](http://flattr.com/thing/344188/balupton-on-Flattr "Donate monthly to this project using Flattr")
[![PayPayl donate button](https://img.shields.io/badge/paypal-donate-yellow.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=QB8GQPZAH84N6 "Donate once-off to this project using Paypal")
[![BitCoin donate button](https://img.shields.io/badge/bitcoin-donate-yellow.svg)](https://coinbase.com/checkouts/9ef59f5479eec1d97d63382c9ebcb93a "Donate once-off to this project using BitCoin")
[![Wishlist browse button](https://img.shields.io/badge/wishlist-donate-yellow.svg)](http://amzn.com/w/2F8TXKSNAFG4V "Buy an item on our wishlist for us")

<!-- /BADGES -->


Copies all files in the raw directory to out.  Useful for large files that cause out of memory error when placed in files directory.


## Install

```
docpad install raw
```


## Configuration
Set as many sources as you want. Path should be relative to the `src` directory. The out folder specified in your [docpad configuration file](http://docpad.org/docs/config) is used for the destination.

If no configuration is specified, defaults to `raw` folder

```
# ...
plugins:
    raw:
        raw:
            src: 'raw'
        app:
            src: 'app'
# ...
```

You can also specify copy options as specified by [ncp package](https://github.com/AvianFlu/ncp):

```
# ...
plugins:
    raw:
        raw:
            src: 'raw'
            options:
                dereference: true    # default in our plugin is `true`
                clobber: false       # default in our plugin is `false`
# ...
```

You can also use a shell command instead of the ncp package if you want:

```
# ...
plugins:
    raw:
        raw:
            command: ['rsync', '-a', './src/raw/', './out/']
# ...
```


<!-- HISTORY/ -->

## History
[Discover the change history by heading on over to the `HISTORY.md` file.](https://github.com/docpad/docpad-plugin-raw/blob/master/HISTORY.md#files)

<!-- /HISTORY -->


<!-- CONTRIBUTE/ -->

## Contribute

[Discover how you can contribute by heading on over to the `CONTRIBUTING.md` file.](https://github.com/docpad/docpad-plugin-raw/blob/master/CONTRIBUTING.md#files)

<!-- /CONTRIBUTE -->


<!-- BACKERS/ -->

## Backers

### Maintainers

These amazing people are maintaining this project:

- Benjamin Lupton <b@lupton.cc> (https://github.com/balupton)
- J. Harshbarger <> (https://github.com/hypercubed)

### Sponsors

No sponsors yet! Will you be the first?

[![Gratipay donate button](https://img.shields.io/gratipay/docpad.svg)](https://www.gratipay.com/docpad/ "Donate weekly to this project using Gratipay")
[![Flattr donate button](https://img.shields.io/badge/flattr-donate-yellow.svg)](http://flattr.com/thing/344188/balupton-on-Flattr "Donate monthly to this project using Flattr")
[![PayPayl donate button](https://img.shields.io/badge/paypal-donate-yellow.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=QB8GQPZAH84N6 "Donate once-off to this project using Paypal")
[![BitCoin donate button](https://img.shields.io/badge/bitcoin-donate-yellow.svg)](https://coinbase.com/checkouts/9ef59f5479eec1d97d63382c9ebcb93a "Donate once-off to this project using BitCoin")
[![Wishlist browse button](https://img.shields.io/badge/wishlist-donate-yellow.svg)](http://amzn.com/w/2F8TXKSNAFG4V "Buy an item on our wishlist for us")

### Contributors

These amazing people have contributed code to this project:

- [Benjamin Lupton](https://github.com/balupton) <b@lupton.cc> — [view contributions](https://github.com/docpad/docpad-plugin-raw/commits?author=balupton)
- [Hypercubed](https://github.com/Hypercubed) — [view contributions](https://github.com/docpad/docpad-plugin-raw/commits?author=Hypercubed)
- [Marcus Stong](https://github.com/stongo) <stongo@gmail.com> — [view contributions](https://github.com/docpad/docpad-plugin-raw/commits?author=stongo)
- [nsonnad](https://github.com/nsonnad) — [view contributions](https://github.com/docpad/docpad-plugin-raw/commits?author=nsonnad)
- [RobLoach](https://github.com/RobLoach) — [view contributions](https://github.com/docpad/docpad-plugin-raw/commits?author=RobLoach)

[Become a contributor!](https://github.com/docpad/docpad-plugin-raw/blob/master/CONTRIBUTING.md#files)

<!-- /BACKERS -->


<!-- LICENSE/ -->

## License

Unless stated otherwise all works are:

- Copyright &copy; 2013+ J. Harshbarger <> (https://github.com/hypercubed)

and licensed under:

- The incredibly [permissive](http://en.wikipedia.org/wiki/Permissive_free_software_licence) [MIT License](http://opensource.org/licenses/mit-license.php)

<!-- /LICENSE -->


