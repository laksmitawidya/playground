// method => obj
// function => global (window, global)

const video = {
    title: 'a',
    play() {
        console.log(this)
    }
}

// 1. METHOD
video.stop = function() {
    console.log(this)
}

// video.stop is a method
video.stop()


// 2. FUNCTION -> will call window object / global
function playVideo() {
    console.log(this)
}

//playVideo here is constructor function (global, window object) -> all of functions have been called
playVideo()


// EXCEPT calling a function using new is different, this will reference with empty object
function VideoPlayer(title) {
    this.title = title
    console.log(this)
}
const v = new VideoPlayer('b');


// show tags is called back function so it will called alwindow too,
const videoTag = {
    title: 'a',
    tags: ['a', 'b', 'c'],
    showTags() {
        // this here is not calling videoTag object, but calling the windows object, the function here is only regular function
        // and not a method, the method here is only showTags() not object function inside the showTags()
        this.tags.forEach(function(tag) {
                console.log(this, tag)
            })
            // so we need to put this outside in order to logged this inside the callback function, but not all method can't read 
            // pass the solution
            // this.tags.forEach(function(tag) {
            //     console.log(this, tag)
            // }, this)
    }
}
videoTag.showTags()