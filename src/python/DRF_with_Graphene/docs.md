I am following this tutorial for using Graphene with Django, and everything was going smooth, until I reached the Integration with Django Rest Framework section.

This section says that you can reuse DRF serializers with Graphene, by creating serializers clones, but it doesn't say what to do with such clones in order to reuse DRF serializers with Graphene.

These are my serializers and clones:

------------

I don't see any reason why we have to do as shown in that tutorial. It is much easier to connect drf and graphql in following way. Doing this way,you do not need to worry about any vague classes and just rely on main aspects of drf and graphene.

Construct drf serializers normally, and connect it to graphql as shown below.

Consider we have model Subject. Let's create CRUD api for it.