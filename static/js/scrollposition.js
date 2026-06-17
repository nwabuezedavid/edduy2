window.wt_scrollposition = function (conf) {
    if (conf.mode === "page" && conf.type === "after" && conf.requestCounter === 1) {
        var scrollPositionConfig = {
            parameterConfiguration : {
                sendAsFigure : "2",
                pageHeight : "3"
            },
            roundResult : true
        };

var pixel=conf.instance,evt="undefined"!==typeof window.unload?"unload":"beforeunload",de=document.documentElement,scrollPosition=window.scrollY+window.innerHeight||self.scrollY+self.innerHeight||de&&de.scrollTop+de.clientHeight||document.body.scrollTop+document.body.clientHeight,isScrollPositionSent=!1,_getYMax=function(){return window.innerHeight+window.scrollMaxY||self.innerHeight+self.scrollMaxY||de&&de.scrollHeight||document.body.offsetHeight};
pixel.registerEvent(window,"scroll",function(){var a=window.scrollY+window.innerHeight||self.scrollY+self.innerHeight||de&&de.scrollTop+de.clientHeight||document.body.scrollTop+document.body.clientHeight;a>scrollPosition&&(scrollPosition=a)});
pixel.registerEvent(window,evt,function(){if(!isScrollPositionSent){isScrollPositionSent=!0;var a=_getYMax();scrollPosition=Math.round(100*(scrollPosition/a));100<scrollPosition&&(scrollPosition=100);if(!isNaN(scrollPosition)){for(;;)if(scrollPositionConfig.roundResult&&0!=scrollPosition%5)scrollPosition++;else break;var b={};b["540"]=""+scrollPosition;scrollPositionConfig.parameterConfiguration.sendAsFigure&&(b[scrollPositionConfig.parameterConfiguration.sendAsFigure]=""+scrollPosition);scrollPositionConfig.parameterConfiguration.pageHeight&&
(b[scrollPositionConfig.parameterConfiguration.pageHeight]=""+a);pixel.sendinfo({linkId:"webtrekk_ignore",customClickParameter:b})}}});

    }
};