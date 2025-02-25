var audio = {
    // Initialize function, runs when the script is loaded
    init: function() {
        var $that = this; // Stores reference to the audio object
        $(function() {  // Runs when the document is ready
            $that.components.media(); // Calls the media component function
        });
    },

    // Object containing different audio-related components
    components: {
        media: function(target) {
            // Selects all <audio> elements with the class 'fc-media'
            // If a target is specified, it searches within that target; otherwise, it defaults to 'body'
            var media = $('audio.fc-media', (target !== undefined) ? target : 'body');
            
            // If there are audio elements found, apply the mediaelementplayer plugin
            if (media.length) {
                media.mediaelementplayer({
                    audioHeight: 40, // Sets the height of the audio player to 40px
                    features: [
                        'playpause',  // Play/Pause button
                        'current',    // Displays current time
                        'duration',   // Shows total duration of the audio
                        'progress',   // Displays progress bar
                        'volume',     // Allows volume control
                        'tracks',     // Supports subtitles/captions (if available)
                        'fullscreen'  // Enables fullscreen (if supported)
                    ],
                    alwaysShowControls: true, // Ensures controls are always visible
                    timeAndDurationSeparator: '<span></span>', // Custom separator between time and duration
                    iPadUseNativeControls: true, // Uses native audio controls on iPad
                    iPhoneUseNativeControls: true, // Uses native controls on iPhone
                    AndroidUseNativeControls: true // Uses native controls on Android devices
                });
            }
        }
    }
};

// Calls the init function to set up the audio player when the page loads
audio.init();
