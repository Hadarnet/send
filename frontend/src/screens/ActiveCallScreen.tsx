import React from 'react';
import { View, Text, Image, Button, StyleSheet } from 'react-native';

const ActiveCallScreen: React.FC = () => {
  const handleMute = () => {
    // Handle mute action
  };

  const handleSpeaker = () => {
    // Handle speaker action
  };

  const handleEndCall = () => {
    // Handle end call action
  };

  return (
    <View style={styles.container}>
      <View style={styles.userInfo}>
        <Image 
          source={{ uri: 'https://user-profile-url.com/caller.jpg' }} 
          style={styles.profileImage} 
        />
        <Text style={styles.callingName}>Amand Call</Text>
        <Text style={styles.callStatus}>Connecting...</Text>
      </View>

      <View style={styles.callActions}>
        <Button title="Mute" onPress={handleMute} />
        <Button title="Speaker" onPress={handleSpeaker} />
        <Button title="End Call" color="red" onPress={handleEndCall} />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#F5F5F5',
  },
  userInfo: {
    alignItems: 'center',
    marginBottom: 40,
  },
  profileImage: {
    width: 100,
    height: 100,
    borderRadius: 50,
  },
  callingName: {
    fontSize: 24,
    fontWeight: 'bold',
    marginTop: 10,
  },
  callStatus: {
    fontSize: 16,
    color: 'gray',
  },
  callActions: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    width: '80%',
  },
});

export default ActiveCallScreen;
