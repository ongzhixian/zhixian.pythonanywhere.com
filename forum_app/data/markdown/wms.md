# WMS notes

sp/ft/ds -> wh -> cus

View application menu item

E:.
├───.venv
│   ├───Include
│   ├───Lib
│   │   └───site-packages

## All modules

'Receiving',
'Received',
'Sending',
'Picking',
'Packing',
'Sent',
'Item_Data',
'Suppliers',
'Customer',
'Location',
'Invoice',
'Credit Note',
'Customer Data'

## General operations

Supplier --> Warehouse Ops --> Customer

WmsFeature
├───WmsSupplierFeature
├───WmsCustomerFeature
├───WmsLocationFeature
├───WmsItemDefinitionFeature
├───WmsReceiveFeature
├───WmsSendFeature
├───WmsInventoryFeature
├───WmsBillingFeature

│   ├───View application menu item  (WMS)
│   ├───View application menu item  -> WMS


WMS Onboarding:

1.  Supplier data
1.  Customer data
1.  Item definition data
1.  Location data
1.  Staff 

Test run:




## Roles 

WMS administrator
WMS data administrator

## Actions (Can...)

│   ├───View application menu item  -> WMS
│   ├───Access WMS sub-module       -> Suppliers / Customers
│   ├───View WMS sub-menu item      (Suppliers)
│   ├───View list (of)              (Suppliers)
│   ├───View detail record (of)     (Suppliers)
│   ├───Add record (of)             (Suppliers)
│   ├───Update record (of)          (Suppliers)
│   ├───Delete record (of)          (Suppliers)


## Roles / Actions


E:.
├───.venv
│   ├───Include
│   ├───Lib
│   │   └───site-packages

LCRUD
00000 0
10000 16 2^4 
01000 8  2^3
00100 4  2^2
00010 2  2^1
00001 1  2^0

USER-ROLES
├───wmsadmin1
│   ├───WMS supplier data administrator
│   ├───WMS customer data administrator
│   ├───WMS item definition data administrator

WMS
├───WMS supplier data administrator
│   ├───View application menu item  (WMS)
│   ├───View WMS sub-menu item      (Suppliers)
│   ├───View list (of)              (Suppliers)
│   ├───View detail record (of)     (Suppliers)
│   ├───Add record (of)             (Suppliers)
│   ├───Update record (of)          (Suppliers)
│   ├───Delete record (of)          (Suppliers)



WMS
├───WMS customer data administrator
│   ├───View application menu item  (WMS)
│   ├───View WMS sub-menu item      (Customers)
│   ├───View list (of)              (Customers)
│   ├───View detail record (of)     (Customers)
│   ├───Add record (of)             (Customers)
│   ├───Update record (of)          (Customers)
│   ├───Delete record (of)          (Customers)


WMS
├───WMS item data administrator
│   ├───View application menu item  (WMS)
│   ├───View WMS sub-menu item      (Item Definition)
│   ├───View list (of)              (Item Definition)
│   ├───View detail record (of)     (Item Definition)
│   ├───Add record (of)             (Item Definition)
│   ├───Update record (of)          (Item Definition)
│   ├───Delete record (of)          (Item Definition)

WMS
├───WMS item inventory administrator
│   ├───View application menu item  (WMS)
│   ├───View WMS sub-menu item      (Inventory)
│   ├───View list (of)              (Inventory)
│   ├───View detail record (of)     (Inventory)
│   ├───Add record (of)             (Inventory)
│   ├───Update record (of)          (Inventory)
│   ├───Delete record (of)          (Inventory)


WMS 
├───WMS location data administrator
│   ├───View application menu item  (WMS)
│   ├───View WMS sub-menu item      (Location)
│   ├───View list (of)              (Location)
│   ├───View detail record (of)     (Location)
│   ├───Add record (of)             (Location)
│   ├───Update record (of)          (Location)
│   ├───Delete record (of)          (Location)




WMS
├───WMS receiving worker (receiver)
│   ├───View application menu item  (WMS)
│   ├───View WMS sub-menu item      (Receiving)


WMS
├───WMS packing worker (packer)
│   ├───View application menu item  (WMS)
│   ├───View WMS sub-menu item      (Packing)





## Location

LocationType
    Warehouse -- Addressable
    Floor
    Section
    Shelf
    Rack
    Bin


"address1": "8629 120TH AVE NE",
"city": "KIRKLAND",
"state": "WA",
"country": "US",
"zipCode": "98033-5865",

country
sector / state
city
address1
address2
postcode


# Reference
https://brunel.figshare.com/articles/dataset/Supply_Chain_Logistics_Problem_Dataset/7558679