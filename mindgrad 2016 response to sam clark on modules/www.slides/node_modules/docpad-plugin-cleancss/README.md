# [Clean CSS](http://github.com/GoalSmashers/clean-css) Plugin for [DocPad](http://docpad.org)

<!-- BADGES/ -->

[![Build Status](https://img.shields.io/travis/docpad/docpad-plugin-cleancss/master.svg)](http://travis-ci.org/docpad/docpad-plugin-cleancss "Check this project's build status on TravisCI")
[![NPM version](https://img.shields.io/npm/v/docpad-plugin-cleancss.svg)](https://npmjs.org/package/docpad-plugin-cleancss "View this project on NPM")
[![NPM downloads](https://img.shields.io/npm/dm/docpad-plugin-cleancss.svg)](https://npmjs.org/package/docpad-plugin-cleancss "View this project on NPM")
[![Dependency Status](https://img.shields.io/david/docpad/docpad-plugin-cleancss.svg)](https://david-dm.org/docpad/docpad-plugin-cleancss)
[![Dev Dependency Status](https://img.shields.io/david/dev/docpad/docpad-plugin-cleancss.svg)](https://david-dm.org/docpad/docpad-plugin-cleancss#info=devDependencies)<br/>
[![Gratipay donate button](https://img.shields.io/gratipay/docpad.svg)](https://www.gratipay.com/docpad/ "Donate weekly to this project using Gratipay")
[![Flattr donate button](https://img.shields.io/badge/flattr-donate-yellow.svg)](http://flattr.com/thing/344188/balupton-on-Flattr "Donate monthly to this project using Flattr")
[![PayPayl donate button](https://img.shields.io/badge/paypal-donate-yellow.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=QB8GQPZAH84N6 "Donate once-off to this project using Paypal")
[![BitCoin donate button](https://img.shields.io/badge/bitcoin-donate-yellow.svg)](https://coinbase.com/checkouts/9ef59f5479eec1d97d63382c9ebcb93a "Donate once-off to this project using BitCoin")
[![Wishlist browse button](https://img.shields.io/badge/wishlist-donate-yellow.svg)](http://amzn.com/w/2F8TXKSNAFG4V "Buy an item on our wishlist for us")

<!-- /BADGES -->


Concatinate and minify CSS files with the `cleancss: true` meta data.


## Install

```bash
docpad install cleancss
```


## Usage

Create a CSS file with the *cleancss* option:

``` css
---
cleancss: true
---

body {
	background-color: black;
}

@import 'example.css';
```


## Configure

### Defaults

The default configuration for this plugin is the equivalant of adding the
following [clean-css options](https://github.com/GoalSmashers/clean-css#how-to-use-clean-css-programmatically)
to your [DocPad configuration file](http://docpad.org/docs/config):

``` coffee
plugins:
	cleancss:
		# These are options passed to the clean-css dependency
		cleancssOpts:
			# * for keeping all (default), 1 for keeping first one only, 0 for
			# removing all
			keepSpecialComments: '*'

			# Whether to keep line breaks (default is false).
			keepBreaks: false

			# Turns on benchmarking mode measuring time spent on cleaning up.
			benchmark: false

			# Whether to process @import rules.
			processImport: true

			# Whether to skip URLs rebasing.
			noRebase: false

			# set to true to disable advanced optimizations.
			noAdvanced: false

			# Enables debug mode.
			debug: false

		# Disabled on development environments by default.
		environments:
			development:
				enabled: false
```


<!-- HISTORY/ -->

## History
[Discover the change history by heading on over to the `HISTORY.md` file.](https://github.com/docpad/docpad-plugin-cleancss/blob/master/HISTORY.md#files)

<!-- /HISTORY -->


<!-- CONTRIBUTE/ -->

## Contribute

[Discover how you can contribute by heading on over to the `CONTRIBUTING.md` file.](https://github.com/docpad/docpad-plugin-cleancss/blob/master/CONTRIBUTING.md#files)

<!-- /CONTRIBUTE -->


<!-- BACKERS/ -->

## Backers

### Maintainers

These amazing people are maintaining this project:

- Benjamin Lupton <b@lupton.cc> (https://github.com/balupton)
- Rob Loach <robloach@gmail.com> (http://github.com/RobLoach)

### Sponsors

No sponsors yet! Will you be the first?

[![Gratipay donate button](https://img.shields.io/gratipay/docpad.svg)](https://www.gratipay.com/docpad/ "Donate weekly to this project using Gratipay")
[![Flattr donate button](https://img.shields.io/badge/flattr-donate-yellow.svg)](http://flattr.com/thing/344188/balupton-on-Flattr "Donate monthly to this project using Flattr")
[![PayPayl donate button](https://img.shields.io/badge/paypal-donate-yellow.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=QB8GQPZAH84N6 "Donate once-off to this project using Paypal")
[![BitCoin donate button](https://img.shields.io/badge/bitcoin-donate-yellow.svg)](https://coinbase.com/checkouts/9ef59f5479eec1d97d63382c9ebcb93a "Donate once-off to this project using BitCoin")
[![Wishlist browse button](https://img.shields.io/badge/wishlist-donate-yellow.svg)](http://amzn.com/w/2F8TXKSNAFG4V "Buy an item on our wishlist for us")

### Contributors

These amazing people have contributed code to this project:

- [Benjamin Lupton](https://github.com/balupton) <b@lupton.cc> — [view contributions](https://github.com/docpad/docpad-plugin-cleancss/commits?author=balupton)
- [Rob Loach](http://github.com/RobLoach) <robloach@gmail.com> — [view contributions](https://github.com/docpad/docpad-plugin-cleancss/commits?author=RobLoach)

[Become a contributor!](https://github.com/docpad/docpad-plugin-cleancss/blob/master/CONTRIBUTING.md#files)

<!-- /BACKERS -->


<!-- LICENSE/ -->

## License

Unless stated otherwise all works are:

- Copyright &copy; 2013+ Rob Loach <robloach@gmail.com> (http://github.com/RobLoach)

and licensed under:

- The incredibly [permissive](http://en.wikipedia.org/wiki/Permissive_free_software_licence) [MIT License](http://opensource.org/licenses/mit-license.php)

<!-- /LICENSE -->


