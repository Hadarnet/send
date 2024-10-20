import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, TouchableOpacity } from 'react-native';
import Icon from 'react-native-vector-icons/Ionicons';
import AudioRecorderPlayer from 'react-native-audio-recorder-player';
import Slider from '@react-native-community/slider';

interface AudioControlProps {
  audioUri: string;
}

const AudioControl: React.FC<AudioControlProps> = ({ audioUri }) => {
  const audioRecorderPlayer = new AudioRecorderPlayer();
  const [isPlaying, setIsPlaying] = useState(false);
  const [currentPositionSec, setCurrentPositionSec] = useState(0);
  const [durationSec, setDurationSec] = useState(0);
  const [formattedPosition, setFormattedPosition] = useState('00:00');
  const [formattedDuration, setFormattedDuration] = useState('00:00');

  useEffect(() => {
    return () => {
      audioRecorderPlayer.stopPlayer();
      audioRecorderPlayer.removePlayBackListener();
    };
  }, []);

  const startPlay = async () => {
    const result = await audioRecorderPlayer.startPlayer(audioUri);
    audioRecorderPlayer.addPlayBackListener((e) => {
      setCurrentPositionSec(e.currentPosition);
      setDurationSec(e.duration);
      setFormattedPosition(audioRecorderPlayer.mmssss(Math.floor(e.currentPosition)));
      setFormattedDuration(audioRecorderPlayer.mmssss(Math.floor(e.duration)));
    });
    setIsPlaying(true);
  };

  const pausePlay = async () => {
    await audioRecorderPlayer.pausePlayer();
    setIsPlaying(false);
  };

  const onSeek = async (value: number) => {
    await audioRecorderPlayer.seekToPlayer(value);
  };

  return (
    <View style={styles.audioContainer}>
      <TouchableOpacity onPress={isPlaying ? pausePlay : startPlay} style={styles.playButton}>
        <Icon name={isPlaying ? 'pause' : 'play'} size={28} color="#FFFFFF" />
      </TouchableOpacity>

      <Slider
        style={styles.slider}
        value={currentPositionSec}
        minimumValue={0}
        maximumValue={durationSec}
        onValueChange={onSeek}
        thumbTintColor="#007AFF"
        minimumTrackTintColor="#007AFF"
        maximumTrackTintColor="#D3D3D3"
      />

      <View style={styles.timeContainer}>
        <Text style={styles.timerText}>{formattedPosition}</Text>
        <Text style={styles.timerText}>{formattedDuration}</Text>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  audioContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#1F2C40',
    padding: 10,
    borderRadius: 20,
    marginVertical: 5,
  },
  playButton: {
    backgroundColor: '#007AFF',
    borderRadius: 50,
    padding: 10,
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 10,
  },
  slider: {
    flex: 1,
    height: 40,
  },
  timeContainer: {
    marginLeft: 10,
    flexDirection: 'row',
    justifyContent: 'space-between',
    width: 60,
  },
  timerText: {
    color: '#FFFFFF',
    fontSize: 12,
  },
});

export default AudioControl;
