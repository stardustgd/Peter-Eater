import MenuComponent from '@/components/MenuComponent'
import { Text } from '@/components/Themed'
import FontAwesome from '@expo/vector-icons/FontAwesome'
import { View, Pressable } from 'react-native'
import { Link } from 'expo-router'

import Colors from '@/constants/Colors'
import { useColorScheme } from '@/components/useColorScheme'

export default function Home() {
  const colorScheme = useColorScheme()

  return (
    <View>
      <Link href="/modal" asChild>
        <Pressable>
          {({ pressed }) => (
            <FontAwesome
              name="info-circle"
              size={25}
              color={Colors[colorScheme ?? 'light'].text}
              style={{
                marginRight: 15,
                opacity: pressed ? 0.5 : 1,
              }}
            />
          )}
        </Pressable>
      </Link>
    </View>
  )
}
