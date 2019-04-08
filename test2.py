from tkinter import Text #, PhotoImage, Tk

class Text_autoReferenceImage(Text):
    def __init__(self,*varg,**kw):
        self.images = {}
        Text.__init__(self,*varg,**kw)

    def image_create(self,index,**options):
        img = options.get("image",None)
        name = Text.image_create(self,index,**options)
        if img is not None:
            self.images[name] = img #this may remove previous reference with same name but different image
        return name

    def delete(self,*varg,**kw):
        Text.delete(self,*varg,**kw)
        self.clean_up_images()

    def clean_up_images(self):
        """deletes reference to all images that are no longer present in Text widget (called by .delete())"""
        images_still_in_use = self.image_names()
        for name in set(self.images.keys()): #need to put .keys() into a set in python3 or it complains about dictionary changing size during iteration
            if name not in images_still_in_use:
                del self.images[name]

    def destroy(self):
        self.images.clear() #remove all references to own images
        return Text.destroy(self)