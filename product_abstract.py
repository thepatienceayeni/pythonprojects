from abc import ABC, abstractmethod


class Product:
    name =""
    type=""
    color=""
    price=""


class ProductAbstract(ABC):
    @abstractmethod 
    def create_product(self, product:Product):
        pass
    
    @abstractmethod 
    def edit_product(self, edit_products):
        pass

    @abstractmethod 
    def get_product_by_id(self, product_id):
        pass

    @abstractmethod
    def get_all_products(self):
        pass

    @abstractmethod 
    def upload_product_image(self, upload_product_image):
        pass

    @abstractmethod
    def delete_product(self, delete_product):
        pass


class ProductManager(ProductAbstract):
        def create_product(self, product:Product):
            print ("Product information") 

        def edit_product(self):
            print ("Hello Buyer, we're launching all products here")

        def get_product_by_id(self, product_id): 
            print ("Welcome to the Launch party")   

        def get_all_products(self): 
            print ("Your first look at all our products")

        def upload_product_image(self, upload_product_image): 
            print ("Preview your product")

        def delete_product(self, delete_product): 
            print ("This product will be deleted")         





product_manager = ProductManager()  
product_manager.create_product(1)
product_manager.edit_product()
product_manager.get_product_by_id(8)
product_manager.get_all_products()
product_manager.upload_product_image(1)
product_manager.delete_product(1)






