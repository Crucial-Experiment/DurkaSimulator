init -2 python:
    import requests, tempfile
    from renpy.display.im import Image

    class RemoteImage(Image):
        """
        This image manipulator loads an image from a URL.
        """
    
        def __init__(self, url, **properties):
            """
            @param url: The url that the image will be loaded from.
            """
    
            super(RemoteImage, self).__init__(url, **properties)
            self.url = url
            
        def load(self, unscaled=False):
            try:
                response = requests.get(self.url)
                response.raise_for_status()

                with tempfile.TemporaryFile() as fp:
                    fp.write(response.content)
                    fp.seek(0)
                    
                    if unscaled:
                        surf = renpy.display.pgrender.load_image_unscaled(fp, self.url)
                    else:
                        surf = renpy.display.pgrender.load_image(fp, self.url)

                return surf
    
            except Exception as e:
                if renpy.config.missing_image_callback:
                    im = renpy.config.missing_image_callback(self.url)
                    if im is None:
                        raise e
    
                    return im.load()
                raise