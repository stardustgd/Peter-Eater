type SubNutrition = {
  Name: string
  Value: string
  Unit: string | null
}

export type Nutrition = {
  Name: string
  Value: string
  Unit: string | null
  SubList: SubNutrition[] | null
}

type Category = {
  DisplayName: string
}

type Product = {
  MarketingName: string
  ShortDescription: string
  LocationId: string
  StationId: string
  Categories: Category[]
  IsGlutenFree: boolean
  IsKosher: boolean
  IsHalal: boolean
  IsVegan: boolean
  IsVegetarian: boolean
  NutritionalTree: Nutrition[]
}

export type Station = {
  StationId: string
  Name: string
}

export type MenuProduct = {
  StationId: string
  MenuStations: Station[]
  Product: Product
}
