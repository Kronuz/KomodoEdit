(function() {
    const log       = require("ko/logging").getLogger("commando-scope-bookmarks")
    const commando  = require("commando/commando");
    const {Cc, Ci}  = require("chrome");

    var local = {};

    log.setLevel(require("ko/logging").LOG_DEBUG);

    var editor = function()
    {
        if ( ! ("editor" in local))
            local.editor = require('ko/editor');
        return local.editor;
    }

    this.onShow = function()
    {
        commando.search("");
    }

    this.onSearch = function(query, uuid, onComplete = null)
    {
        log.debug(uuid + " - Starting Scoped Search");

        var view = ko.views.manager.currentView;
        var bookmarks = editor().getAllMarks();
        var results = [];

        for (let line in bookmarks)
        {
            if (query != "" && query != line && bookmarks[line].indexOf(query) == -1)
                continue;

            results.push({
                classList: "compact",
                id: view.uid + line,
                name: "line " + line,
                description: bookmarks[line],
                icon: "chrome://icomoon/skin/icons/arrow-right14.png",
                scope: "scope-bookmarks",
                allowMultiSelect: false,
                data: {
                    line: line
                }
            });
        }

        log.debug(uuid + " " + results.length + " results");

        if (results)
            commando.renderResults(results, uuid);

        if (onComplete)
            onComplete(uuid);
        else
            commando.onSearchComplete(uuid);
    }

    this.onSelectResult = function(selectedItems)
    {
        var item = selectedItems.slice(0)[0];
        var line = item.resultData.data.line;
        var e = editor();

        e.setCursor(e.getLineEndPos(line));

        commando.hideCommando();
        ko.commands.doCommandAsync('cmd_focusEditor');
    }

}).apply(module.exports);