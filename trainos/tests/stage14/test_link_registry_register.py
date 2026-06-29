from trainos.kernel.intelligence.knowledge_linking.knowledge_link import KnowledgeLink
from trainos.kernel.intelligence.knowledge_linking.link_registry import LinkRegistry
from trainos.kernel.intelligence.knowledge_linking.link_type import LinkType


def test_link_registry_register():

    registry = LinkRegistry()

    link = KnowledgeLink(
        source="water",
        target="food",
        type=LinkType.CAUSES,
    )
    registry.register(link)
    assert registry.links() == (link,)
