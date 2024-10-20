import React from 'react';
import { View, Text, StyleSheet, Image, StyleProp, ViewStyle, TextStyle, ImageStyle } from 'react-native';

interface ChatItemProps {
  contactName: string;
  profilePicture: string;
  lastMessage: string;
  lastMessageDate: string;
  unreadCount: number;
  containerStyle?: StyleProp<ViewStyle>;
  nameStyle?: StyleProp<TextStyle>;
  dateStyle?: StyleProp<TextStyle>;
  messageStyle?: StyleProp<TextStyle>;
  imageStyle?: StyleProp<ImageStyle>;
  unreadBadgeStyle?: StyleProp<ViewStyle>;
  unreadTextStyle?: StyleProp<TextStyle>;
}

const ChatItem: React.FC<ChatItemProps> = ({
  contactName,
  profilePicture,
  lastMessage,
  lastMessageDate,
  unreadCount,
  containerStyle,
  nameStyle,
  dateStyle,
  messageStyle,
  imageStyle,
  unreadBadgeStyle,
  unreadTextStyle,
}) => {
  return (
    <View style={[styles.container, containerStyle]}>
      <Image source={{ uri: profilePicture }} style={[styles.image, imageStyle]} />
      <View style={styles.details}>
        <View style={styles.header}>
          <Text style={[styles.name, nameStyle]}>{contactName}</Text>
          <Text style={[styles.date, dateStyle]}>{lastMessageDate}</Text>
        </View>
        <Text style={[styles.message, messageStyle]} numberOfLines={1}>
          {lastMessage}
        </Text>
      </View>
      {unreadCount > 0 && (
        <View style={[styles.unreadBadge, unreadBadgeStyle]}>
          <Text style={[styles.unreadText, unreadTextStyle]}>{unreadCount}</Text>
        </View>
      )}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flexDirection: 'row',
    padding: 15,
    backgroundColor: '#3A0078',
    borderRadius: 8,
    alignItems: 'center',
    marginVertical: 5,
  },
  image: {
    width: 50,
    height: 50,
    borderRadius: 25,
    borderWidth: 2,
    borderColor: '#5A2A83',
    marginRight: 15,
  },
  details: {
    flex: 1,
  },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
  },
  name: {
    fontSize: 16,
    color: '#fff',
    fontWeight: 'bold',
  },
  date: {
    fontSize: 12,
    color: '#ccc',
  },
  message: {
    fontSize: 14,
    color: '#ccc',
    marginTop: 2,
  },
  unreadBadge: {
    backgroundColor: '#FF6B6B',
    borderRadius: 12,
    paddingHorizontal: 8,
    paddingVertical: 4,
  },
  unreadText: {
    color: '#fff',
    fontSize: 12,
  },
});

export default ChatItem;
