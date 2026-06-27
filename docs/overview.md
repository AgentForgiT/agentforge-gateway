# Overview

AgentForge Gateway is the central routing layer between developer tools and AI model providers.

It exists so users can configure one local or hosted endpoint, then connect tools such as IDE assistants, coding agents, scripts, and research workflows to a consistent API.

## Core Idea

Many tools already understand the OpenAI API shape. Gateway v1 should preserve that compatibility while allowing AgentForge to route to different providers behind the scenes.

## Primary Users

- developers using multiple AI coding tools
- researchers comparing provider behavior
- teams that want one controlled API entry point
- builders who need local, free-tier, and paid model options behind one interface

## First Principle

The gateway should make provider switching boring.

Provider differences belong in adapters. Tool-facing clients should see a predictable API.
