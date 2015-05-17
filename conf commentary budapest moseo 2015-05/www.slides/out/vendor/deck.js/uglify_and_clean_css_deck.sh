#!/bin/bash

uglifyjs deck.core.js deck.events.js deck.fit.js deck.menu.js deck.hash.js deck.notes.js deck.slide-clone.js deck.step.js deck.events.js deck.velocity.js -c -o deck.all.min.js

cleancss -o deck.all.min.css deck.core.css deck.menu.css deck.hash.css deck.notes.css

