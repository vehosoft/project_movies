def movie_image_upload_location(instance, filename):
    return 'media/movies/images/%s.png' % (instance.id)