import React, { useState } from 'react';
import { View, FlatList, StyleSheet, Image, TouchableOpacity, Text, ScrollView } from 'react-native';
import CustomTextInput from '../components/CustomTextInput'; // Adjust the import path as necessary

interface Contact {
  id: string;
  name: string;
  status: string;
  lastSeen: string;
  online: boolean;
  avatar: string;
  lastMessage: string;
}

interface Group {
  id: string;
  name: string;
  lastMessage: string;
  online: boolean;
  avatar: string;
}

const contacts: Contact[] = [
  { id: '1', lastMessage: 'Hello, how are you?', name: 'Athalia Putri', status: 'Last seen yesterday', lastSeen: 'yesterday', online: false, avatar: 'https://w7.pngwing.com/pngs/7/618/png-transparent-man-illustration-avatar-icon-fashion-men-avatar-face-fashion-girl-heroes-thumbnail.png' },
  { id: '2', lastMessage: 'Hello, how are you?', name: 'Erlan Sadewa', status: 'Online', lastSeen: '', online: true, avatar: 'https://w7.pngwing.com/pngs/7/618/png-transparent-man-illustration-avatar-icon-fashion-men-avatar-face-fashion-girl-heroes-thumbnail.png' },
  // More contacts...
];

const groups: Group[] = [
  { id: '1', lastMessage: 'Group chat message', name: 'Family', online: false, avatar: 'https://w7.pngwing.com/pngs/7/618/png-transparent-man-illustration-avatar-icon-fashion-men-avatar-face-fashion-girl-heroes-thumbnail.png' },
  { id: '2', lastMessage: 'Group chat message', name: 'Work', online: true, avatar: 'https://w7.pngwing.com/pngs/7/618/png-transparent-man-illustration-avatar-icon-fashion-men-avatar-face-fashion-girl-heroes-thumbnail.png' },
  // More groups...
];

const ChatsScreen: React.FC = () => {
  const Stories = () => (
    <ScrollView horizontal style={styles.storiesContainer}>
      <View style={styles.story}>
        <TouchableOpacity style={styles.storyIcon}>
          <Text style={styles.addStoryText}>+</Text>
        </TouchableOpacity>
        <Text style={styles.storyText}>Your Story</Text>
      </View>
      {contacts.map(contact => (
        <View key={contact.id} style={styles.story}>
          <Image source={{ uri: contact.avatar }} style={styles.storyImage} />
          <Text style={styles.storyText}>{contact.name.split(' ')[0]}</Text>
        </View>
      ))}
    </ScrollView>
  );

  const [searchQuery, setSearchQuery] = useState<string>('');

  // Filter contacts based on search query
  const filteredContacts = contacts.filter(contact =>
    contact.name.toLowerCase().includes(searchQuery.toLowerCase())
  );

  // Filter groups based on search query
  const filteredGroups = groups.filter(group =>
    group.name.toLowerCase().includes(searchQuery.toLowerCase())
  );

  return (
    <View style={styles.container}>
      <Text style={{ color: '#FFFFFF', fontSize: 24, fontWeight: 'bold', marginVertical: 10 }}>
        Chats
      </Text>
      <View>
        <Stories />
      </View>
      <CustomTextInput
        placeholder="Search by name..."
        value={searchQuery}
        onChangeText={setSearchQuery} // Update search query
        iconName="search-outline" // Optional: add an icon for search
      />

      {/* Contact List */}
      <ScrollView>
        <FlatList
          data={filteredContacts}
          keyExtractor={(item) => item.id}
          renderItem={({ item }) => (
            <TouchableOpacity style={styles.contactItem}>
              <View style={styles.contactDetails}>
                <Image source={{ uri: item.avatar }} style={styles.avatar} />
                <View style={styles.textContainer}>
                  <Text style={styles.contactName}>{item.name}</Text>
                  <Text style={styles.contactStatus}>{item.lastMessage}</Text>
                </View>
              </View>
              {item.online && <View style={styles.onlineIndicator} />}
            </TouchableOpacity>
          )}
        />

        <Text style={{ color: '#FFFFFF', fontSize: 24, fontWeight: 'bold', marginVertical: 10 }} >Contacts</Text>
        {/* Group List */}
        <FlatList
          data={filteredGroups}
          keyExtractor={(item) => item.id}
          renderItem={({ item }) => (
            <TouchableOpacity style={styles.contactItem}>
              <View style={styles.contactDetails}>
                <Image source={{ uri: item.avatar }} style={styles.avatar} />
                <View style={styles.textContainer}>
                  <Text style={styles.contactName}>{item.name}</Text>
                  <Text style={styles.contactStatus}>{item.lastMessage}</Text>
                </View>
              </View>
              {item.online && <View style={styles.onlineIndicator} />}
            </TouchableOpacity>
          )}
        />
      </ScrollView>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#0E1624',
    padding: 10,
  },
  contactItem: {
    flexDirection: 'row',
    alignItems: 'center',
    padding: 15,
    borderBottomWidth: 1,
    borderBottomColor: '#1F2C40',
    justifyContent: 'space-between',
  },
  contactDetails: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  avatar: {
    width: 50,
    height: 50,
    borderRadius: 25,
    marginRight: 15,
  },
  textContainer: {
    justifyContent: 'center',
  },
  contactName: {
    fontSize: 18,
    color: '#FFFFFF',
    fontWeight: 'bold',
  },
  contactStatus: {
    fontSize: 14,
    color: '#A0AABF',
  },
  onlineIndicator: {
    width: 12,
    height: 12,
    borderRadius: 6,
    backgroundColor: '#00FF00',
    position: 'absolute',
    right: 10,
  },
  storiesContainer: {
    flexDirection: 'row',
    marginBottom: 10,
  },
  story: {
    alignItems: 'center',
    marginRight: 15,
  },
  storyIcon: {
    width: 60,
    height: 60,
    borderRadius: 30,
    backgroundColor: '#1F2C40',
    justifyContent: 'center',
    alignItems: 'center',
  },
  addStoryText: {
    color: '#00FF00',
    fontSize: 24,
  },
  storyImage: {
    width: 60,
    height: 60,
    borderRadius: 30,
  },
  storyText: {
    marginTop: 5,
    color: '#FFFFFF',
    fontSize: 12,
    textAlign: 'center',
  },
});

export default ChatsScreen;
