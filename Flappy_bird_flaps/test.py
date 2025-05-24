import neat

def tiny_network():
    # Load configuration
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                        neat.DefaultSpeciesSet, neat.DefaultStagnation,
                        'tiny_config.txt')
    
    # Create and configure a genome
    genome = neat.DefaultGenome(1)
    genome.configure_new(config.genome_config)
    
    # Create neural network from genome
    net = neat.nn.FeedForwardNetwork.create(genome, config)
    
    # Test the network
    decision = net.activate([0.5])[0]
    print(f"Output: {decision:.4f} ->", "Flap!" if decision > 0.5 else "Don't flap!")

tiny_network()