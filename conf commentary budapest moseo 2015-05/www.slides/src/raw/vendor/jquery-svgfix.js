//- modify jQuery so that addClass and removeClass work for svg elements
//- modified from: https://github.com/kbwood/svg
//- license: MIT

(function($) { // Hide scope, no $ conflict

var  svgNS = 'http://www.w3.org/2000/svg';
var isSVGElem = function(node) {
  return (node.nodeType == 1 && node.namespaceURI == svgNS);
};

/* Support adding class names to SVG nodes. */
$.fn.addClass = function(origAddClass) {
        return function(classNames) {
                classNames = classNames || '';
                return this.each(function() {
                        if (isSVGElem(this)) {
                                var node = this;
                                $.each(classNames.split(/\s+/), function(i, className) {
                                        var classes = (node.className ? node.className.baseVal : node.getAttribute('class'));
                                        if ($.inArray(className, classes.split(/\s+/)) == -1) {
                                                classes += (classes ? ' ' : '') + className;
                                                (node.className ? node.className.baseVal = classes :
                                                        node.setAttribute('class',  classes));
                                        }
                                });
                        }
                        else {
                                origAddClass.apply($(this), [classNames]);
                        }
                });
        };
}($.fn.addClass);

/* Support removing class names from SVG nodes. */
$.fn.removeClass = function(origRemoveClass) {
        return function(classNames) {
                classNames = classNames || '';
                return this.each(function() {
                        if (isSVGElem(this)) {
                                var node = this;
                                $.each(classNames.split(/\s+/), function(i, className) {
                                        var classes = (node.className ? node.className.baseVal : node.getAttribute('class'));
                                        classes = $.grep(classes.split(/\s+/), function(n, i) { return n != className; }).
                                                join(' ');
                                        (node.className ? node.className.baseVal = classes :
                                                node.setAttribute('class', classes));
                                });
                        }
                        else {
                                origRemoveClass.apply($(this), [classNames]);
                        }
                });
        };
}($.fn.removeClass);})(jQuery)