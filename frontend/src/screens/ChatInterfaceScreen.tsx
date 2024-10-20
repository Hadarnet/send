import React, { useState, useEffect } from 'react';
import {
  View,
  FlatList,
  StyleSheet,
  TextInput,
  TouchableOpacity,
  Text,
  KeyboardAvoidingView,
  Platform,
  Alert,
  Modal,
  Image,
} from 'react-native';
import Slider from '@react-native-community/slider';
import Icon from 'react-native-vector-icons/Ionicons';
import DocumentPicker from 'react-native-document-picker';
import AudioRecorderPlayer from 'react-native-audio-recorder-player';

interface Message {
  id: string;
  text?: string;
  sender: 'me' | 'them';
  timestamp: number;
  imageUrl?: string;
  voiceNote?: string;
  documentName?: string;
}

const ChatInterfaceScreen: React.FC = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [message, setMessage] = useState<string>('');
  const [modalVisible, setModalVisible] = useState(false);
  const [isRecording, setIsRecording] = useState(false);
  const [isPlaying, setIsPlaying] = useState(false);
  const [currentVoiceNote, setCurrentVoiceNote] = useState<string | null>(null);
  const [currentPositionSec, setCurrentPositionSec] = useState<number>(0);
  const [durationSec, setDurationSec] = useState<number>(0);
  const [audioRecorderPlayer] = useState(new AudioRecorderPlayer()); // Create a single instance
  const [recordedVoice, setRecordedVoice] = useState<string | null>(null);

  // Send text message
  const sendMessage = () => {
    if (message.trim() === '') return;

    const newMessage: Message = {
      id: Math.random().toString(),
      text: message,
      sender: 'me',
      timestamp: Date.now(),
    };

    setMessages((prevMessages) => [...prevMessages, newMessage]);
    setMessage('');
  };

  // Open modal for media options
  const openModal = () => {
    setModalVisible(true);
  };

  const closeModal = () => {
    setModalVisible(false);
  };

  // Record voice note
  const recordVoiceNote = async () => {
    try {
      if (!isRecording) {
        const result = await audioRecorderPlayer.startRecorder();
        setIsRecording(true);
        setRecordedVoice(result);
        console.log('Recording started:', result);

        audioRecorderPlayer.addRecordBackListener((e) => {
          setCurrentPositionSec(e.currentPosition);
          setDurationSec(e.duration);
        });
      } else {
        const result = await audioRecorderPlayer.stopRecorder();
        setIsRecording(false);
        setRecordedVoice(result);
        console.log('Recording stopped:', result);
        audioRecorderPlayer.removeRecordBackListener(); // Clean up listener
        sendVoiceNote(result);
      }
    } catch (error) {
      console.error('Error in recordVoiceNote:', error);
      Alert.alert('Error starting/stopping voice recording');
    }
  };

  // Send voice note
  const sendVoiceNote = (uri: string) => {
    const newMessage: Message = {
      id: Math.random().toString(),
      sender: 'me',
      timestamp: Date.now(),
      voiceNote: uri,
    };
    setMessages((prevMessages) => [...prevMessages, newMessage]);
    closeModal();
  };

  // Send image
  const sendImage = async () => {
    const result = await launchImageLibrary({
      mediaType: 'photo',
    });

    if (!result.didCancel && result.assets && result.assets.length > 0) {
      const newMessage: Message = {
        id: Math.random().toString(),
        sender: 'me',
        timestamp: Date.now(),
        imageUrl: result.assets[0].uri,
      };
      setMessages((prevMessages) => [...prevMessages, newMessage]);
    }
    closeModal();
  };

  // Send document
  const sendDocument = async () => {
    try {
      const result = await DocumentPicker.pick({
        type: [DocumentPicker.types.allFiles],
      });

      const newMessage: Message = {
        id: Math.random().toString(),
        sender: 'me',
        timestamp: Date.now(),
        documentName: result[0].name,
      };
      setMessages((prevMessages) => [...prevMessages, newMessage]);
    } catch (err) {
      if (DocumentPicker.isCancel(err)) {
        console.log('User canceled the document picker');
      } else {
        console.log('Unknown error', err);
      }
    }
    closeModal();
  };

  const handleCall = () => {
    Alert.alert('Calling feature is not implemented yet.');
  };

  // Play voice note
  const playVoiceNote = async (voiceNote: string) => {
    if (isPlaying) {
      await audioRecorderPlayer.stopPlayer();
      audioRecorderPlayer.removePlayBackListener(); // Clean up listener
      setIsPlaying(false);
      setCurrentVoiceNote(null);
      return;
    }

    audioRecorderPlayer.addPlayBackListener((e: any) => {
      setCurrentPositionSec(e.currentPosition);
      setDurationSec(e.duration);
    });

    setCurrentVoiceNote(voiceNote);
    await audioRecorderPlayer.startPlayer(voiceNote);
    setIsPlaying(true);
  };

  const renderMessageItem = ({ item }: { item: Message }) => (
    <View
      style={[
        styles.messageContainer,
        item.sender === 'me' ? styles.myMessage : styles.theirMessage,
      ]}
    >
      {item.text ? (
        <Text style={styles.messageText}>{item.text}</Text>
      ) : item.imageUrl ? (
        <Image source={{ uri: item.imageUrl }} style={styles.messageImage} />
      ) : item.voiceNote ? (
        <View style={styles.voiceNoteContainer}>
          <TouchableOpacity onPress={() => playVoiceNote(item.voiceNote!)}>
            <Icon name={isPlaying && currentVoiceNote === item.voiceNote ? 'pause' : 'play'} size={24} color="#FFFFFF" />
          </TouchableOpacity>
          <Slider
            style={styles.slider}
            minimumValue={0}
            maximumValue={durationSec}
            value={currentPositionSec}
            onSlidingComplete={async (value) => {
              await audioRecorderPlayer.seekToPlayer(Math.floor(value));
            }}
          />
          <Text style={styles.voiceNoteDuration}>
            {Math.floor(currentPositionSec / 1000)}s / {Math.floor(durationSec / 1000)}s
          </Text>
        </View>
      ) : item.documentName ? (
        <Text style={styles.messageText}>Document: {item.documentName}</Text>
      ) : null}
    </View>
  );

  return (
    <View style={styles.container}>
      {/* Header */}
      <View style={styles.header}>
        <TouchableOpacity onPress={handleCall}>
          <Icon name="call" size={24} color="#FFFFFF" />
        </TouchableOpacity>
        <Text style={styles.contactName}>Athalia Putri</Text>
        <TouchableOpacity onPress={handleCall}>
          <Icon name="search" size={24} color="#FFFFFF" />
        </TouchableOpacity>
      </View>

      {/* Message List */}
      <FlatList
        data={messages}
        renderItem={renderMessageItem}
        keyExtractor={(item) => item.id}
        style={styles.messageList}
      />

      {/* Input Area */}
      <KeyboardAvoidingView
        behavior={Platform.OS === 'ios' ? 'padding' : undefined}
        keyboardVerticalOffset={Platform.OS === 'ios' ? 100 : 0}
      >
        <View style={styles.inputContainer}>
          <TouchableOpacity onPress={openModal}>
            <Icon name="add-circle-outline" size={30} color="#FFFFFF" />
          </TouchableOpacity>
          <TextInput
            style={styles.input}
            value={message}
            onChangeText={setMessage}
            placeholder="Type a message"
            placeholderTextColor="#A9A9A9"
          />
          <TouchableOpacity onPress={sendMessage}>
            <Icon name="send" size={24} color="#007AFF" />
          </TouchableOpacity>
        </View>
      </KeyboardAvoidingView>

      {/* Modal for voice note, image, document */}
      <Modal
        transparent={true}
        visible={modalVisible}
        animationType="slide"
        onRequestClose={closeModal}
      >
        <View style={styles.modalContainer}>
          <View style={styles.modalContent}>
            <TouchableOpacity style={styles.modalButton} onPress={recordVoiceNote}>
              <Text style={styles.modalText}>
                {isRecording ? 'Stop Recording Voice Note' : 'Record Voice Note'}
              </Text>
            </TouchableOpacity>
            <TouchableOpacity style={styles.modalButton} onPress={sendImage}>
              <Text style={styles.modalText}>Send Image</Text>
            </TouchableOpacity>
            <TouchableOpacity style={styles.modalButton} onPress={sendDocument}>
              <Text style={styles.modalText}>Send Document</Text>
            </TouchableOpacity>
            <TouchableOpacity style={styles.modalButton} onPress={closeModal}>
              <Text style={styles.modalText}>Close</Text>
            </TouchableOpacity>
          </View>
        </View>
      </Modal>
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#121212' },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    backgroundColor: '#1E1E1E',
    padding: 10,
  },
  contactName: { color: '#FFFFFF', fontSize: 18 },
  messageList: { paddingHorizontal: 10 },
  messageContainer: {
    marginVertical: 5,
    padding: 10,
    borderRadius: 10,
    maxWidth: '80%',
  },
  myMessage: { backgroundColor: '#007AFF', alignSelf: 'flex-end' },
  theirMessage: { backgroundColor: '#444', alignSelf: 'flex-start' },
  messageText: { color: '#FFFFFF' },
  messageImage: {
    width: 150,
    height: 150,
    borderRadius: 10,
    marginVertical: 5,
  },
  voiceNoteContainer: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  slider: { flex: 1, height: 40, marginHorizontal: 10 },
  voiceNoteDuration: { color: '#FFFFFF' },
  inputContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#1E1E1E',
    padding: 10,
  },
  input: {
    flex: 1,
    backgroundColor: '#3C3C3C',
    color: '#FFFFFF',
    borderRadius: 20,
    paddingHorizontal: 10,
    marginHorizontal: 10,
  },
  modalContainer: {
    flex: 1,
    justifyContent: 'center',
    backgroundColor: 'rgba(0,0,0,0.7)',
  },
  modalContent: {
    backgroundColor: '#1E1E1E',
    marginHorizontal: 20,
    borderRadius: 10,
    padding: 20,
  },
  modalButton: {
    padding: 15,
    borderRadius: 10,
    backgroundColor: '#007AFF',
    alignItems: 'center',
    marginVertical: 5,
  },
  modalText: {
    color: '#FFFFFF',
    fontSize: 16,
  },
});

export default ChatInterfaceScreen;
