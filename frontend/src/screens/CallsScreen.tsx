import React from 'react';
import { View, Text, FlatList, Image, StyleSheet } from 'react-native';

interface Call {
  id: string;
  name: string;
  type: 'Incoming' | 'Outgoing' | 'Missed';
  date: string;
  image: string;
}

const calls: Call[] = [
  { id: '1', name: 'LG', type: 'Incoming', date: 'Sept 1', image: 'https://user-profile-url.com/lg.jpg' },
  { id: '2', name: 'Samsung', type: 'Outgoing', date: 'Sept 3', image: 'https://user-profile-url.com/samsung.jpg' },
  { id: '3', name: 'Apple', type: 'Missed', date: 'Sept 5', image: 'https://user-profile-url.com/apple.jpg' },
];

const CallsScreen: React.FC = () => {
  return (
    <View style={styles.container}>
      <FlatList
        data={calls}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => (
          <View style={styles.callItem}>
            <Image source={{ uri: item.image }} style={styles.profileImage} />
            <View>
              <Text style={styles.callName}>{item.name}</Text>
              <Text style={styles.callType}>{item.type} - {item.date}</Text>
            </View>
          </View>
        )}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#FFFFFF',
    padding: 10,
  },
  callItem: {
    flexDirection: 'row',
    padding: 10,
    borderBottomWidth: 1,
    borderBottomColor: '#EEE',
  },
  profileImage: {
    width: 50,
    height: 50,
    borderRadius: 25,
    marginRight: 15,
  },
  callName: {
    fontSize: 18,
    fontWeight: 'bold',
  },
  callType: {
    fontSize: 14,
    color: 'gray',
  },
});

export default CallsScreen;
