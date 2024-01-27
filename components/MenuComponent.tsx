import React, { useState } from 'react'
import { Button, StyleSheet, SafeAreaView, SectionList, StatusBar, TouchableOpacity } from 'react-native'

import { Text, View } from './Themed'

const DATA = [
  {
    title: 'Main dishes',
    data: ['Pizza', 'Burger', 'Risotto'],
  },
  {
    title: 'Sides',
    data: ['French Fries', 'Onion Rings', 'Fried Shrimps'],
  },
  {
    title: 'Drinks',
    data: ['Water', 'Coke', 'Beer'],
  },
  {
    title: 'Desserts',
    data: ['Cheese Cake', 'Ice Cream'],
    review: ['test', 'test'],
  },
]

const sampleMenu =
  [
    {
      station: "Home",
      foods: [
        {
          "foodName": "Chicken Teriyaki",
          "foodDescription": "Stir-fried chicken, broccoli, cabbage, carrot, celery and onion tossed with teriyaki sauce",
          "calories": "130",
          "category": "Entr\u00c3\u00a9es"
        },
        {
          "foodName": "Jasmine Rice",
          "foodDescription": "Thai long grain rice with aromatic, nutty flavor",
          "calories": "50",
          "category": "Sides"
        },
        {
          "foodName": "Steamed Fresh Broccoli",
          "foodDescription": "Steamed fresh broccoli florets",
          "calories": "20",
          "category": "Sides"
        },
        {
          "foodName": "Teriyaki Sauce",
          "foodDescription": "Blend of soy sauce, sesame and spices",
          "calories": "45",
          "category": "Condiments"
        }
      ]
    },
    {
      "station": "Oven",
      "foods": [
        {
          "foodName": "Classic Cheese Pizza",
          "foodDescription": "Mozzarella cheese and pizza sauce on a golden brown crust",
          "calories": "340",
          "category": "Pizza"
        },
        {
          "foodName": "Meat Lover's Pizza",
          "foodDescription": "Pepperoni, Italian sausage, Italian meatballs, mozzarella and pizza sauce",
          "calories": "350",
          "category": "Pizza"
        },
        {
          "foodName": "Pepperoni Pizza",
          "foodDescription": "Pepperoni, mozzarella and pizza sauce on a golden brown crust",
          "calories": "370",
          "category": "Pizza"
        }
      ]
    },
    {
      "station": "Sizzle Grill",
      "foods": [
        {
          "foodName": "Crispy Shoestring French Fries",
          "foodDescription": "Thin-cut potatoes, deep-fried to golden brown",
          "calories": "190",
          "category": "Sides"
        },
        {
          "foodName": "American Cheese",
          "foodDescription": "Sliced American cheese",
          "calories": "N/A",
          "category": "Protein"
        },
        {
          "foodName": "Breaded Chicken Breast (1  each)",
          "foodDescription": "Crispy breaded chicken",
          "calories": "260",
          "category": "Protein"
        },
        {
          "foodName": "Cheddar Cheese",
          "foodDescription": "Sliced Cheddar cheese",
          "calories": "N/A",
          "category": "Protein"
        },
        {
          "foodName": "Gardenburger Black Bean Burger (1  each)",
          "foodDescription": "Vegan black bean burger",
          "calories": "110",
          "category": "Protein"
        },
        {
          "foodName": "Angus Beef Patty (1  each)",
          "foodDescription": "Angus beef patty",
          "calories": "420",
          "category": "Protein"
        },
        {
          "foodName": "Hamburger Roll (1  each)",
          "foodDescription": "Soft split roll",
          "calories": "140",
          "category": "Grains "
        },
        {
          "foodName": "Sliced Red Onions",
          "foodDescription": "Thinly sliced red onions",
          "calories": "N/A",
          "category": "Salads"
        },
        {
          "foodName": "Sliced Tomatoes",
          "foodDescription": "Sliced fresh tomatoes",
          "calories": "N/A",
          "category": "Salads"
        },
        {
          "foodName": "Lettuce",
          "foodDescription": "Fresh lettuce leaves",
          "calories": "N/A",
          "category": "Salads"
        },
        {
          "foodName": "Dill Pickle Slices",
          "foodDescription": "Dill pickle slices",
          "calories": "N/A",
          "category": "Condiments"
        }
      ]
    },
    {
      "station": "Vegan",
      "foods": [
        {
          "foodName": "Spicy Tofu Vegetable Stir-Fry",
          "foodDescription": "Tofu sauteed in sesame oil blend with red and green peppers, red onion and chili garlic sauce",
          "calories": "170",
          "category": "Entr\u00c3\u00a9es"
        }
      ]
    },
    {
      "station": "Bakery",
      "foods": [
        {
          "foodName": "Vanilla Iced Donut with Sprinkles",
          "foodDescription": "Freshly baked donut topped with vanilla icing and rainbow sprinkles",
          "calories": "460",
          "category": "Breads"
        },
        {
          "foodName": "Danish Pastry",
          "foodDescription": "Warm Danish pastry",
          "calories": "150",
          "category": "Breads"
        },
        {
          "foodName": "Iced Cinnamon Roll",
          "foodDescription": "Freshly baked cinnamon roll with cream cheese icing",
          "calories": "220",
          "category": "Breads"
        }
      ]
    }
  ]


const styles = StyleSheet.create({
  container: {
    flex: 1,
    width: 500,
    paddingTop: StatusBar.currentHeight,
    marginHorizontal: 16,
  },
  item: {
    backgroundColor: '#0064a4',
    padding: 20,
    marginVertical: 8,
  },
  header: {
    fontSize: 32,
    backgroundColor: '#fff',
  },
  title: {
    fontSize: 24,
    color: '#ffffff',
  },
  itemTouchable: {
    borderRadius: 10,
    overflow: 'hidden',
  },
})

export default function MenuComponent({ data = DATA }) {
  return (
    <SafeAreaView style={styles.container}>
      <SectionList
        sections={data}
        keyExtractor={(item, index) => item + index}
        renderItem={({ item }) => (
          <View>
            <TouchableOpacity
              onPress={() => console.log(`pressed ${item}`)}
              style={styles.item}>
              <Text style={styles.title}>{item}</Text>
            </TouchableOpacity>
          </View>
        )
        }
        renderSectionHeader={({ section: { title } }) => (
          <Text style={styles.header}>{title}</Text>
        )}
      />
    </SafeAreaView >
  )
}
