import { Button } from "@/components/ui/button"
import { Card, CardContent } from "@/components/ui/card"
import { ModeToggle } from "./components/mode-toggle"

export const App = () => {
  return (
    <div className="min-h-screen bg-background text-foreground flex flex-col">
      <header className="w-full border-b border-border/50">
        <nav className="max-w-6xl mx-auto flex items-center justify-between py-4 px-6">
          <span className="text-xl font-semibold">MyCloud</span>
          <div className="flex items-center gap-3">
            <Button variant="ghost">Login</Button>
            <Button>Get Started</Button>
            <ModeToggle />
          </div>
        </nav>
      </header>

      <main className="flex-1 max-w-6xl mx-auto flex flex-col items-center justify-center text-center px-6 py-24">
        <h1 className="text-4xl md:text-6xl font-bold tracking-tight">
          Deploy apps globally in seconds.
        </h1>
        <p className="text-muted-foreground max-w-xl mt-4 text-lg">
          MyCloud gives you edge deployments, instant rollbacks, logs, and analytics — all from one platform.
        </p>
        <div className="flex gap-4 mt-8">
          <Button size="lg" className="px-6">Start Now</Button>
          <Button size="lg" variant="secondary" className="px-6">Documentation</Button>
        </div>
      </main>

      <section className="w-full py-20 border-t border-border/50 bg-muted/20">
        <div className="max-w-6xl mx-auto px-6 grid grid-cols-1 md:grid-cols-3 gap-6">
          {[
            {
              title: "Global Edge",
              desc: "Deploy from anywhere to everywhere in under a second.",
            },
            {
              title: "Auto Scaling",
              desc: "Effortlessly scale as traffic spikes without intervention.",
            },
            {
              title: "Instant Rollbacks",
              desc: "Revert deployments instantly with zero downtime.",
            },
          ].map((feature, i) => (
            <Card key={i} className="border-border/50 bg-card">
              <CardContent className="p-6 space-y-2">
                <h3 className="text-lg font-semibold">{feature.title}</h3>
                <p className="text-muted-foreground text-sm leading-relaxed">
                  {feature.desc}
                </p>
              </CardContent>
            </Card>
          ))}
        </div>
      </section>

      <footer className="w-full border-t border-border/50 py-6">
        <div className="max-w-6xl mx-auto px-6 flex justify-between text-sm text-muted-foreground">
          <span>© 2026 MyCloud</span>
          <div className="flex gap-4">
            <a href="#" className="hover:text-foreground">Terms</a>
            <a href="#" className="hover:text-foreground">Privacy</a>
          </div>
        </div>
      </footer>
    </div>
  )
}
